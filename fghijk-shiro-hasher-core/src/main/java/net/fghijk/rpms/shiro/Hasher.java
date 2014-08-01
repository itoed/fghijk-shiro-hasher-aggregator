package net.fghijk.rpms.shiro;

import org.apache.shiro.authc.credential.DefaultPasswordService;
import org.apache.shiro.crypto.hash.DefaultHashService;

public class Hasher {
    public static void main(String[] args) {
        DefaultHashService hashService = new DefaultHashService();
        hashService.setHashIterations(1024);
        hashService.setGeneratePublicSalt(true);

        DefaultPasswordService passwordService = new DefaultPasswordService();
        passwordService.setHashService(hashService);

        if (args.length == 1) {
            String encryptedPassword = passwordService.encryptPassword(args[0]);
            System.out.println(encryptedPassword);
        }

        if (args.length > 1) {
            if (passwordService.passwordsMatch(args[0], args[1])) {
                System.out.println("Password " + args[0] + " matches "
                        + args[1]);
            } else {
                System.out.println("Password " + args[0] + " does not match "
                        + args[1]);
                System.exit(1);
            }
        }
    }
}