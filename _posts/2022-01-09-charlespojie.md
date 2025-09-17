---
layout: post
title: "charles 破解"
date: 2021-01-09
categories: [其他]
tags: [charles,抓包,破解]
author: zhangshuming
---

# charles 破解

## 目录

1. [第一步,下载charles](#第一步,下载charles)
1. [第二部,生成key,这里使用的是java代码](#第二部,生成key,这里使用的是java代码)
1. [第三步,查看破解码](#第三步,查看破解码)
1. [第四步，破解](#第四步，破解)

---

# 第一步,下载charles
<a href="https://www.charlesproxy.com/download/" target="_blank">下载charles</a>
# 第二部,生成key,这里使用的是java代码
```
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Random;
 
public class test {
    private static final int ROUNDS = 12;
    private static final int ROUND_KEYS = 2 * (ROUNDS + 1);
    private static final Random rand = new Random();
 
    public static void main(String[] args) {
        rand.setSeed(System.nanoTime());
        //  这里填入你需要的name,随意填
        String name = "ylv51234";
        System.out.println("name: " + name + "    key: " + crack(name));
    }
 
    private static String crack(String text) {
        byte[] name = text.getBytes();
        int length = name.length + 4;
        int padded = ((-length) & (8 - 1)) + length;
        ByteBuffer buffer = ByteBuffer.allocate(padded);
        buffer.order(ByteOrder.BIG_ENDIAN);
        buffer.putInt(name.length);
        buffer.put(name);
 
        long ckName = 0x7a21c951691cd470L;
        long ckKey = -5408575981733630035L;
        CkCipher ck = new CkCipher(ckName);
        ByteBuffer outBuffer = ByteBuffer.allocate(padded);
        outBuffer.order(ByteOrder.BIG_ENDIAN);
 
        for (int i = 0; i < padded; i += 8) {
            long nowVar = buffer.getLong(i);
            long dd = ck.encrypt(nowVar);
            outBuffer.putLong(dd);
        }
 
        int n = 0;
        for (byte b : outBuffer.array()) {
            n = rotateLeft(n ^ (int) b, 3);
        }
        int prefix = n ^ 0x54882f8a;
        int suffix = rand.nextInt();
        long in = ((long) prefix << 32) | (suffix & 0xffffffffL);
        if ((suffix >> 16) == 0x0401 || (suffix >> 16) == 0x0402 || (suffix >> 16) == 0x0403) {
            // Keep `in` as is
        } else {
            in = (in & 0xffffffff00000000L) | 0x01000000L | (suffix & 0xffffff);
        }
 
        long out = new CkCipher(ckKey).decrypt(in);
        long n2 = 0;
        for (int i = 56; i >= 0; i -= 8) {
            n2 ^= (in >> i) & 0xff;
        }
 
        int vv = (int) (n2 & 0xff);
        if (vv < 0) vv = -vv;
        return String.format("%02x%016x", vv, out);
    }
 
    private static class CkCipher {
        private int[] rk = new int[ROUND_KEYS];
 
        public CkCipher(long ckKey) {
            int[] ld = new int[]{(int) ckKey, (int) (ckKey >>> 32)};
            rk[0] = -1209970333;
            for (int i = 1; i < ROUND_KEYS; i++) {
                rk[i] = rk[i - 1] - 1640531527;
            }
            int a = 0, b = 0, i = 0, j = 0;
            for (int k = 0; k < 3 * ROUND_KEYS; k++) {
                rk[i] = rotateLeft(rk[i] + (a + b), 3);
                a = rk[i];
                ld[j] = rotateLeft(ld[j] + (a + b), a + b);
                b = ld[j];
                i = (i + 1) % ROUND_KEYS;
                j = (j + 1) % 2;
            }
        }
 
        public long encrypt(long in) {
            int a = (int) in + rk[0];
            int b = (int) (in >>> 32) + rk[1];
            for (int r = 1; r <= ROUNDS; r++) {
                a = rotateLeft(a ^ b, b) + rk[2 * r];
                b = rotateLeft(b ^ a, a) + rk[2 * r + 1];
            }
            return packLong(a, b);
        }
 
        public long decrypt(long in) {
            int a = (int) in;
            int b = (int) (in >>> 32);
            for (int i = ROUNDS; i > 0; i--) {
                b = rotateRight(b - rk[2 * i + 1], a) ^ a;
                a = rotateRight(a - rk[2 * i], b) ^ b;
            }
            b -= rk[1];
            a -= rk[0];
            return packLong(a, b);
        }
    }
 
    private static int rotateLeft(int x, int y) {
        return (x << (y & 31)) | (x >>> (32 - (y & 31)));
    }
 
    private static int rotateRight(int x, int y) {
        return (x >>> (y & 31)) | (x << (32 - (y & 31)));
    }
 
    private static long packLong(int a, int b) {
        return ((long) a & 0xffffffffL) | ((long) b << 32);
    }
}
```
# 第三步,查看破解码
<a href="/assets/charlespojie/Snipaste_2025-07-25_11-22-59.png"></a>
# 第四步，破解

<a href="/assets/charlespojie/Snipaste_2025-07-25_11-26-14.png"></a>