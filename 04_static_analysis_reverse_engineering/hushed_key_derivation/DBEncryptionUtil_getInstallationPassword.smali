# Lcom/hushed/base/repository/database/DBEncryptionUtil; -> getInstallationPassword(Landroid/content/SharedPreferences;)[C

    const/4 v0, 0
    const-string v1, "KEY_DB_INFO_STORE"
    invoke-interface v4, v1, v0, Landroid/content/SharedPreferences;->getString(Ljava/lang/String; Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0
    if-nez v0, +015h
    invoke-static Ljava/util/UUID;->randomUUID()Ljava/util/UUID;
    move-result-object v0
    invoke-virtual v0, Ljava/util/UUID;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-interface v4, Landroid/content/SharedPreferences;->edit()Landroid/content/SharedPreferences$Editor;
    move-result-object v4
    invoke-interface v4, v1, v0, Landroid/content/SharedPreferences$Editor;->putString(Ljava/lang/String; Ljava/lang/String;)Landroid/content/SharedPreferences$Editor;
    move-result-object v4
    invoke-interface v4, Landroid/content/SharedPreferences$Editor;->apply()V
    new-instance v4, Ljava/lang/StringBuilder;
    invoke-direct v4, Ljava/lang/StringBuilder;-><init>()V
    invoke-virtual v4, v0, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v0, "com.hushed.release"
    invoke-virtual v4, v0, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual v4, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v4
    const-string v0, "UTF-8"
    invoke-virtual v4, v0, Ljava/lang/String;->getBytes(Ljava/lang/String;)[B
    move-result-object v4
    const-string v0, "SHA-1"
    invoke-static v0, Ljava/security/MessageDigest;->getInstance(Ljava/lang/String;)Ljava/security/MessageDigest;
    move-result-object v0
    invoke-virtual v0, v4, Ljava/security/MessageDigest;->update([B)V
    invoke-virtual v0, Ljava/security/MessageDigest;->digest()[B
    move-result-object v4
    goto +5h
    move-exception v0
    invoke-static v0, Lb9/p;->c(Ljava/lang/Throwable;)V
    const/16 v0, 16
    new-array v1, v0, [C
    const/4 v2, 0
    if-ge v2, v0, +010h
    aget-byte v3, v4, v2
    and-int/lit16 v3, v3, 255
    rem-int/lit8 v3, v3, 94
    add-int/lit8 v3, v3, 33
    int-to-char v3, v3
    aput-char v3, v1, v2
    add-int/lit8 v2, v2, 1
    goto -fh
    return-object v1
    move-exception v4
    invoke-static v4, Lb9/p;->c(Ljava/lang/Throwable;)V
    new-instance v0, Ljava/lang/RuntimeException;
    invoke-direct v0, v4, Ljava/lang/RuntimeException;-><init>(Ljava/lang/Throwable;)V
    throw v0
