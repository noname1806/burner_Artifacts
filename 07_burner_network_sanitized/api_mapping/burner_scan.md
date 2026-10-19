# Forensic & Privacy Static Scan Report
_Generated: 2025-09-12T08:38:07.852281Z_

**Heuristic APCI Score:** `0.0/100` (higher is better)


## Summary

| Severity | Count |
|---|---:|
| high | 92 |
| medium | 234 |
| low | 148 |

**By Category:** android: 52, crypto: 15, privacy: 317, secrets: 90

## Findings

### CRYPTO_AES_ECB (high)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzwd.java:16`
```
return zzwv.zza.zza("AES/ECB/NOPADDING");
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_AES_ECB.

### CRYPTO_AES_ECB (high)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzxn.java:21`
```
return zzwv.zza.zza("AES/ECB/NoPadding");
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_AES_ECB.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\BuildConfig.java:6`
```
public static final String ADJUST_APP_TOKEN = "jg2mq6epansw";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\BuildConfig.java:10`
```
public static final String BRAZE_API_KEY = "00000000-0000-0000-0000-000000000017";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\analytics\tracker\TrackerAttribution.java:56`
```
return "TrackerAttribution(name=" + this.name + ", token=" + this.token + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\login\LoginMethod.java:143`
```
return "Sso(firebaseToken=" + this.firebaseToken + ", ssoProvider=" + this.ssoProvider + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\models\models\StorePurchaseModel.java:249`
```
return "Pending(sku=" + productId + ", token=" + strM9231toStringimpl + ", orderId=" + (str == null ? AbstractJsonLexerKt.NULL : OrderId.m9212toStringimpl(str)) + ", price=" + this.price + ", receipt=" + this.receipt + ", isPending=" + this.isPending + ", isAcknowledged=" + this.isAcknowledged + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\models\models\StorePurchaseModel.java:482`
```
return "Active(sku=" + productId + ", token=" + strM9231toStringimpl + ", orderId=" + (str == null ? AbstractJsonLexerKt.NULL : OrderId.m9212toStringimpl(str)) + ", price=" + this.price + ", receipt=" + this.receipt + ", isPending=" + this.isPending + ", isAcknowledged=" + this.isAcknowledged + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\network\generated\models\RegisterSsoRequest.java:95`
```
return "RegisterSsoRequest(trackingId=" + this.trackingId + ", clientFeatures=" + this.clientFeatures + ", firebaseInstallId=" + this.firebaseInstallId + ", trackerToken=" + this.trackerToken + ", trackerName=" + this.trackerName + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\network\generated\models\Sip.java:59`
```
return "Sip(uri=" + this.uri + ", password=" + this.password + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\network\generated\models\User.java:208`
```
return "User(createdSample=" + this.createdSample + ", credits=" + this.credits + ", dateCreated=" + this.dateCreated + ", id=" + this.id + ", lastUpdatedDate=" + this.lastUpdatedDate + ", platform=" + this.platform + ", superUser=" + this.superUser + ", totalNumberBurners=" + this.totalNumberBurners + ", trackingId=" + this.trackingId + ", appVersion=" + this.appVersion + ", carrierName=" + this.carrierName + ", clientFeatures=" + this.clientFeatures + ", countryCode=" + this.countryCode + ", eligibleForPaywall=" + this.eligibleForPaywall + ", firebaseInstallId=" + this.firebaseInstallId + ", lifetimeSubscriptions=" + this.lifetimeSubscriptions + ", phoneNumber=" + this.phoneNumber + ", pushToken=" + this.pushToken + ", registrationId=" + this.registrationId + ", selector=" + this.selector + ", sip=" + this.sip + ", version=" + this.version + ", voipPushToken=" + this.voipPushToken + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\network\generated\models\User.java:208`
```
return "User(createdSample=" + this.createdSample + ", credits=" + this.credits + ", dateCreated=" + this.dateCreated + ", id=" + this.id + ", lastUpdatedDate=" + this.lastUpdatedDate + ", platform=" + this.platform + ", superUser=" + this.superUser + ", totalNumberBurners=" + this.totalNumberBurners + ", trackingId=" + this.trackingId + ", appVersion=" + this.appVersion + ", carrierName=" + this.carrierName + ", clientFeatures=" + this.clientFeatures + ", countryCode=" + this.countryCode + ", eligibleForPaywall=" + this.eligibleForPaywall + ", firebaseInstallId=" + this.firebaseInstallId + ", lifetimeSubscriptions=" + this.lifetimeSubscriptions + ", phoneNumber=" + this.phoneNumber + ", pushToken=" + this.pushToken + ", registrationId=" + this.registrationId + ", selector=" + this.selector + ", sip=" + this.sip + ", version=" + this.version + ", voipPushToken=" + this.voipPushToken + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\network\models\PhoneRegistrationResponse.java:57`
```
return "PhoneRegistrationResponse(authToken=" + this.authToken + ", user=" + this.user + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\network\models\RegisterParams.java:107`
```
return "RegisterParams(appVersion=" + this.appVersion + ", code=" + this.code + ", country=" + this.country + ", phoneNumber=" + this.phoneNumber + ", platform=" + this.platform + ", trackerName=" + this.trackerName + ", trackerToken=" + this.trackerToken + ", trackingId=" + this.trackingId + ", firebaseInstallId=" + this.firebaseInstallId + ", clientFeatures=" + this.clientFeatures + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\network\models\RegisterResponse.java:58`
```
return "RegisterResponse(firebaseToken=" + this.firebaseToken + ", user=" + this.user + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\network\models\SipRegistration.java:69`
```
return "SipRegistration(domains=" + this.domains + ", password=" + this.password + ", username=" + this.username + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\preboard\model\PostAuthPreboardType.java:47`
```
return "Sso(token=" + this.token + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\repositories\call\voip\models\VoipUserModel.java:78`
```
return "VoipUserModel(accountId=" + this.accountId + ", identity=" + this.identity + ", password=" + this.password + ", sipURI=" + this.sipURI + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\libs\firebase\auth\FirebaseLoginMethod.java:50`
```
return "CustomToken(token=" + this.token + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\libs\firebase\auth\FirebaseLoginMethod.java:102`
```
return "Facebook(token=" + this.token + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\libs\firebase\auth\FirebaseLoginMethod.java:151`
```
return "Google(token=" + this.token + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\libs\firebase\auth\ForceRefreshFirebaseToken.java:133`
```
java.lang.String r2 = "Error when refreshing firebase token: "
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\libs\firebase\config\FirebaseConfig.java:111`
```
return "FirebaseConfig(apiKey=" + this.apiKey + ", applicationId=" + this.applicationId + ", databaseUrl=" + this.databaseUrl + ", gcmSenderId=" + this.gcmSenderId + ", projectId=" + this.projectId + ", storageBucket=" + this.storageBucket + ", signInOauthClientId=" + this.signInOauthClientId + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\SharedPreferencesManager.java:21`
```
private static final String PREFS_KEY_PUSH_TOKEN = "push_token";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\id\FileIdentityStorage.java:16`
```
public static final String API_KEY = "api_key";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\id\FileIdentityStorage.java:18`
```
public static final String EXPERIMENT_API_KEY = "experiment_api_key";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\id\IdentityConfiguration.java:107`
```
return "IdentityConfiguration(instanceName=" + this.instanceName + ", apiKey=" + ((Object) this.apiKey) + ", experimentApiKey=" + ((Object) this.experimentApiKey) + ", identityStorageProvider=" + this.identityStorageProvider + ", storageDirectory=" + this.storageDirectory + ", logger=" + this.logger + PropertyUtils.MAPPED_DELIM2;
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\id\IdentityConfiguration.java:107`
```
return "IdentityConfiguration(instanceName=" + this.instanceName + ", apiKey=" + ((Object) this.apiKey) + ", experimentApiKey=" + ((Object) this.experimentApiKey) + ", identityStorageProvider=" + this.identityStorageProvider + ", storageDirectory=" + this.storageDirectory + ", logger=" + this.logger + PropertyUtils.MAPPED_DELIM2;
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\android\billingclient\api\BillingClientImpl.java:199`
```
com.google.android.gms.internal.play_billing.zzb.zzj("BillingClient", "Continuation token: ".concat(String.valueOf(string)));
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\android\billingclient\api\BillingClientImpl.java:405`
```
com.google.android.gms.internal.play_billing.zzb.zzj("BillingClient", "Continuation token: ".concat(String.valueOf(string)));
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\android\billingclient\api\BillingClientImpl.java:916`
```
com.google.android.gms.internal.play_billing.zzb.zzj("BillingClient", "Consuming purchase with token: " + purchaseToken);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\android\billingclient\api\ConsumeResult.java:70`
```
return "ConsumeResult(billingResult=" + this.zza + ", purchaseToken=" + this.zzb + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\braze\configuration\BrazeConfig.java:1145`
```
StringBuilder sb = new StringBuilder("Builder(apiKey=");
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\braze\push\BrazeFirebaseMessagingService.java:56`
```
return Intrinsics.stringPlus("No configured API key, not registering token in onNewToken. Token: ", newToken);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\braze\push\BrazeFirebaseMessagingService.java:68`
```
return Intrinsics.stringPlus("Automatic FirebaseMessagingService.OnNewToken() registration disabled, not registering token: ", newToken);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\braze\push\BrazeFirebaseMessagingService.java:80`
```
return Intrinsics.stringPlus("Registering Firebase push token in onNewToken. Token: ", newToken);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\braze\support\StringUtils.java:64`
```
return "Generating MD5 for user id: " + this.b + " apiKey: " + ((Object) this.c);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\AccessToken.java:236`
```
sb.append("{AccessToken token:");
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\AccessTokenManager.java:36`
```
public static final String EXTRA_NEW_ACCESS_TOKEN = "com.facebook.sdk.EXTRA_NEW_ACCESS_TOKEN";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\AccessTokenManager.java:37`
```
public static final String EXTRA_OLD_ACCESS_TOKEN = "com.facebook.sdk.EXTRA_OLD_ACCESS_TOKEN";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\AuthenticationTokenManager.java:21`
```
public static final String EXTRA_NEW_AUTHENTICATION_TOKEN = "com.facebook.sdk.EXTRA_NEW_AUTHENTICATION_TOKEN";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\AuthenticationTokenManager.java:22`
```
public static final String EXTRA_OLD_AUTHENTICATION_TOKEN = "com.facebook.sdk.EXTRA_OLD_AUTHENTICATION_TOKEN";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\GraphRequest.java:1367`
```
StringBuilder sb = new StringBuilder("{Request:  accessToken: ");
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\appevents\iap\InAppPurchaseEventManager.java:38`
```
private static final String INAPP_CONTINUATION_TOKEN = "INAPP_CONTINUATION_TOKEN";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\appevents\internal\Constants.java:35`
```
public static final String IAP_PURCHASE_TOKEN = "fb_iap_purchase_token";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\internal\NativeProtocol.java:65`
```
public static final String EXTRA_ACCESS_TOKEN = "com.facebook.platform.extra.ACCESS_TOKEN";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\internal\NativeProtocol.java:68`
```
public static final String EXTRA_AUTHENTICATION_TOKEN = "com.facebook.platform.extra.ID_TOKEN";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\internal\NativeProtocol.java:138`
```
public static final String RESULT_ARGS_ACCESS_TOKEN = "access_token";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\internal\ServerProtocol.java:24`
```
public static final String DIALOG_PARAM_ACCESS_TOKEN = "access_token";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\internal\ServerProtocol.java:26`
```
public static final String DIALOG_PARAM_AUTHENTICATION_TOKEN = "id_token";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\login\LoginResult.java:88`
```
return "LoginResult(accessToken=" + this.accessToken + ", authenticationToken=" + this.authenticationToken + ", recentlyGrantedPermissions=" + this.recentlyGrantedPermissions + ", recentlyDeniedPermissions=" + this.recentlyDeniedPermissions + PropertyUtils.MAPPED_DELIM2;
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\login\LoginResult.java:88`
```
return "LoginResult(accessToken=" + this.accessToken + ", authenticationToken=" + this.authenticationToken + ", recentlyGrantedPermissions=" + this.recentlyGrantedPermissions + ", recentlyDeniedPermissions=" + this.recentlyDeniedPermissions + PropertyUtils.MAPPED_DELIM2;
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\share\internal\ShareConstants.java:30`
```
public static final String EXTRA_UNLIKE_TOKEN = "com.facebook.platform.extra.UNLIKE_TOKEN";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\api\identity\SaveAccountLinkingTokenRequest.java:19`
```
public static final String EXTRA_TOKEN = "extra_token";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\api\signin\internal\zbb.java:40`
```
HttpURLConnection httpURLConnection = (HttpURLConnection) new URL("https://accounts.google.com/o/oauth2/revoke?token=" + this.zbb).openConnection();
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\data\DataBufferUtils.java:11`
```
public static final String KEY_NEXT_PAGE_TOKEN = "next_page_token";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\data\DataBufferUtils.java:12`
```
public static final String KEY_PREV_PAGE_TOKEN = "prev_page_token";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\internal\ServiceSpecificExtraArgs.java:17`
```
public static final String WINDOW_TOKEN = "com.google.android.gms.games.key.popupWindowToken";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\server\response\FastParser.java:362`
```
throw new ParseException("Unexpected token: " + cZai);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\server\response\FastParser.java:520`
```
throw new ParseException("Unexpected token: " + cZai);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\server\response\FastParser.java:536`
```
throw new ParseException("Unexpected token: " + cZai2);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\server\response\FastParser.java:602`
```
throw new ParseException("Unexpected token: " + cZai);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\server\response\FastParser.java:640`
```
throw new ParseException("Unexpected token: " + cZai);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzacv.java:39`
```
Log.e("LocalRequestInterceptor", "Unexpected error getting App Check token: " + e.getMessage());
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzaej.java:44`
```
return "RevokeTokenRequest{providerId=" + this.zza + ", tenantId=" + this.zzb + ", token=" + this.zzc + ", tokenType=" + String.valueOf(this.zzd) + ", idToken=" + this.zze + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzaej.java:44`
```
return "RevokeTokenRequest{providerId=" + this.zza + ", tenantId=" + this.zzb + ", token=" + this.zzc + ", tokenType=" + String.valueOf(this.zzd) + ", idToken=" + this.zze + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzags.java:125`
```
sb.append("id_token=").append(this.zzc).append("&");
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzags.java:128`
```
sb.append("access_token=").append(this.zzd).append("&");
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzags.java:134`
```
sb.append("oauth_token_secret=").append(this.zzh).append("&");
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\GenericIdpActivity.java:106`
```
Log.e("GenericIdpActivity", "Unexpected error getting App Check token: " + task.getException().getMessage());
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\RecaptchaActivity.java:85`
```
Log.e(zzb, "Unexpected error getting App Check token: " + task.getException().getMessage());
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zzk.java:35`
```
return "AttestationResult{recaptchaV2Token=" + this.zza + ", playIntegrityToken=" + this.zzb + ", recaptchaEnterpriseToken=" + this.zzc + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zzk.java:35`
```
return "AttestationResult{recaptchaV2Token=" + this.zza + ", playIntegrityToken=" + this.zzb + ", recaptchaEnterpriseToken=" + this.zzc + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zzk.java:35`
```
return "AttestationResult{recaptchaV2Token=" + this.zza + ", playIntegrityToken=" + this.zzb + ", recaptchaEnterpriseToken=" + this.zzc + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\crashlytics\internal\common\AutoValue_InstallIdProvider_InstallIds.java:36`
```
return "InstallIds{crashlyticsInstallId=" + this.crashlyticsInstallId + ", firebaseInstallationId=" + this.firebaseInstallationId + ", firebaseAuthenticationToken=" + this.firebaseAuthenticationToken + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\crashlytics\internal\model\AutoValue_CrashlyticsReport.java:96`
```
return "CrashlyticsReport{sdkVersion=" + this.sdkVersion + ", gmpAppId=" + this.gmpAppId + ", platform=" + this.platform + ", installationUuid=" + this.installationUuid + ", firebaseInstallationId=" + this.firebaseInstallationId + ", firebaseAuthenticationToken=" + this.firebaseAuthenticationToken + ", appQualitySessionId=" + this.appQualitySessionId + ", buildVersion=" + this.buildVersion + ", displayVersion=" + this.displayVersion + ", session=" + this.session + ", ndkPayload=" + this.ndkPayload + ", appExitInfo=" + this.appExitInfo + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\installations\AutoValue_InstallationTokenResult.java:33`
```
return "InstallationTokenResult{token=" + this.token + ", tokenExpirationTimestamp=" + this.tokenExpirationTimestamp + ", tokenCreationTimestamp=" + this.tokenCreationTimestamp + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\installations\local\AutoValue_PersistedInstallationEntry.java:62`
```
return "PersistedInstallationEntry{firebaseInstallationId=" + this.firebaseInstallationId + ", registrationStatus=" + this.registrationStatus + ", authToken=" + this.authToken + ", refreshToken=" + this.refreshToken + ", expiresInSecs=" + this.expiresInSecs + ", tokenCreationEpochInSecs=" + this.tokenCreationEpochInSecs + ", fisError=" + this.fisError + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\installations\local\AutoValue_PersistedInstallationEntry.java:62`
```
return "PersistedInstallationEntry{firebaseInstallationId=" + this.firebaseInstallationId + ", registrationStatus=" + this.registrationStatus + ", authToken=" + this.authToken + ", refreshToken=" + this.refreshToken + ", expiresInSecs=" + this.expiresInSecs + ", tokenCreationEpochInSecs=" + this.tokenCreationEpochInSecs + ", fisError=" + this.fisError + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\installations\remote\AutoValue_InstallationResponse.java:47`
```
return "InstallationResponse{uri=" + this.uri + ", fid=" + this.fid + ", refreshToken=" + this.refreshToken + ", authToken=" + this.authToken + ", responseCode=" + this.responseCode + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\installations\remote\AutoValue_InstallationResponse.java:47`
```
return "InstallationResponse{uri=" + this.uri + ", fid=" + this.fid + ", refreshToken=" + this.refreshToken + ", authToken=" + this.authToken + ", responseCode=" + this.responseCode + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\installations\remote\AutoValue_TokenResult.java:33`
```
return "TokenResult{token=" + this.token + ", tokenExpirationTimestamp=" + this.tokenExpirationTimestamp + ", responseCode=" + this.responseCode + "}";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\FirebaseMessagingService.java:18`
```
static final String ACTION_NEW_TOKEN = "com.google.firebase.messaging.NEW_TOKEN";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\GmsRpc.java:48`
```
private static final String PARAM_FIS_AUTH_TOKEN = "Goog-Firebase-Installations-Auth";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\Store.java:102`
```
Log.w(Constants.TAG, "Failed to parse token: " + e);
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\remoteconfig\RemoteConfigConstants.java:26`
```
public static final String INSTANCE_ID_TOKEN = "appInstanceIdToken";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionInfo.java:79`
```
return "SessionInfo(sessionId=" + this.sessionId + ", firstSessionId=" + this.firstSessionId + ", sessionIndex=" + this.sessionIndex + ", eventTimestampUs=" + this.eventTimestampUs + ", dataCollectionStatus=" + this.dataCollectionStatus + ", firebaseInstallationId=" + this.firebaseInstallationId + ", firebaseAuthenticationToken=" + this.firebaseAuthenticationToken + PropertyUtils.MAPPED_DELIM2;
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\gson\reflect\TypeToken.java:154`
```
sb.append("but got: ").append(type.getClass().getName()).append(", for type token: ").append(type.toString()).append('.');
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\a\c\e\g\w\e.java:90`
```
return "Success(token=" + this.f770a + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\core\model\RegisterPushTokenRequestBodyApi.java:79`
```
return "RegisterPushTokenRequestBodyApi(token=" + this.token + ", platform=" + this.platform + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GENERIC (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\domain\model\TokenApi.java:55`
```
return "TokenApi(token=" + this.token + ")";
```
- **Why it matters:** Possible secret detected by pattern SECRET_GENERIC.

### SECRET_GOOGLE_API (high)
- **Category:** secrets
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\libs\firebase\config\ProdFirebaseConfigKt.java:9`
```
private static final FirebaseConfig prodFirebaseConfig = new FirebaseConfig("AIzaSyAAM3cxVOun-5aZXd0rcKk7vTGPWkP-fq0", "1:84028889562:android:013a80e68c4bb7cc2c48e3", "https://burner-prod-default-rtdb.firebaseio.com", "84028889562", "burner-prod", "burner-prod.appspot.com", "84028889562-o6cl86ij1rpuobnssi9il3b6j0aok8ts.apps.googleusercontent.com");
```
- **Why it matters:** Possible secret detected by pattern SECRET_GOOGLE_API.

### ANDROID_EXTERNAL_STORAGE (medium)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\internal\Utility.java:1261`
```
StatFs statFs = new StatFs(Environment.getExternalStorageDirectory().getPath());
```
- **Why it matters:** Write/read on external/shared storage found; data may be forensically accessible.

### ANDROID_EXTERNAL_STORAGE (medium)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\internal\Utility.java:1272`
```
StatFs statFs = new StatFs(Environment.getExternalStorageDirectory().getPath());
```
- **Why it matters:** Write/read on external/shared storage found; data may be forensically accessible.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\bumptech\glide\load\engine\cache\MemorySizeCalculator.java:50`
```
Log.d(TAG, "Calculation complete, Calculated memory cache size: " + toMb(this.memoryCacheSize) + ", pool size: " + toMb(this.bitmapPoolSize) + ", byte array size: " + toMb(i) + ", memory class limited? " + (i3 > maxSize) + ", max size: " + toMb(maxSize) + ", memoryClass: " + builder.activityManager.getMemoryClass() + ", isLowMemoryDevice: " + isLowMemoryDevice(builder.activityManager));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\bumptech\glide\load\engine\executor\RuntimeCompat.java:37`
```
Log.e(TAG, "Failed to calculate accurate cpu count", th);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\bumptech\glide\load\resource\bitmap\DefaultImageHeaderParser.java:241`
```
Log.d(TAG, "Unable to skip enough data, type: " + ((int) uInt8) + ", wanted to skip: " + uInt16 + ", but actually skipped: " + jSkip);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\bumptech\glide\load\resource\bitmap\Downsampler.java:185`
```
Log.v(TAG, "Calculated target [" + iRound + "x" + iRound2 + "] for source [" + i7 + "x" + i8 + "], sampleSize: " + i10 + ", targetDensity: " + options.inTargetDensity + ", density: " + options.inDensity + ", density multiplier: " + f);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\bumptech\glide\load\resource\bitmap\Downsampler.java:295`
```
Log.v(TAG, "Calculate scaling, source: [" + i2 + "x" + i3 + "], degreesToRotate: " + i + ", target: [" + i4 + "x" + i5 + "], power of two scaled: [" + iFloor + "x" + iFloor2 + "], exact scale factor: " + scaleFactor + ", power of 2 sample size: " + iMax + ", adjusted scale factor: " + scaleFactor2 + ", target density: " + options.inTargetDensity + ", density: " + options.inDensity);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\bumptech\glide\load\resource\bitmap\HardwareConfigState.java:158`
```
Log.w("Downsampler", "Excluding HARDWARE bitmap config because we're over the file descriptor limit, file descriptors " + length + ", limit " + maxFdCount);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\GraphRequest.java:1391`
```
Log.w(TAG, "Starting with v13 of the SDK, a client token must be embedded in your client code before making Graph API calls. Visit https://developers.facebook.com/docs/android/getting-started#client-token to learn how to implement this change.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\appevents\UserDataStore.java:499`
```
Log.e(TAG, "Setting email failure: this is not a valid email address");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\appevents\internal\AutomaticAnalyticsLogger.java:154`
```
Log.e(TAG, "Error parsing in-app subscription data.", e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\GoogleAuthUtil.java:74`
```
Log.w("GoogleAuthUtil", "Error when getting token", e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\GoogleAuthUtil.java:78`
```
Log.w("GoogleAuthUtil", "Error when getting token", e2);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\UserRecoverableAuthException.java:32`
```
Log.w("Auth", "Make sure that an intent was provided to class instantiation.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\UserRecoverableAuthException.java:36`
```
Log.e("Auth", "This shouldn't happen. Gms API throwing this exception should support the recovery Intent.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\UserRecoverableAuthException.java:42`
```
Log.e("Auth", "this instantiation of UserRecoverableAuthException doesn't support an Intent.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\api\signin\internal\SignInHubActivity.java:51`
```
Log.w("AuthSignInClient", "Could not launch sign in Intent. Google Play Service is probably being updated...");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\api\signin\internal\SignInHubActivity.java:75`
```
Log.e("AuthSignInClient", "Google account is null");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\api\signin\internal\SignInHubActivity.java:106`
```
Log.e("AuthSignInClient", "Null action");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\api\signin\internal\SignInHubActivity.java:111`
```
Log.e("AuthSignInClient", "Action not implemented");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\api\signin\internal\SignInHubActivity.java:116`
```
Log.e("AuthSignInClient", "Unknown action: ".concat(String.valueOf(intent.getAction())));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\api\signin\internal\SignInHubActivity.java:122`
```
Log.e("AuthSignInClient", "Activity started with no configuration.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\api\signin\internal\SignInHubActivity.java:129`
```
Log.e("AuthSignInClient", "Activity started with invalid configuration.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\api\signin\internal\SignInHubActivity.java:155`
```
Log.e("AuthSignInClient", "Sign in result data cannot be null");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\zzl.java:241`
```
Log.i("GoogleAuthUtil", "Error on service connection.", e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\auth\zzl.java:248`
```
Log.w("GoogleAuthUtil", String.format("SecurityException while bind to auth service: %s", e2.getMessage()));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzp.java:34`
```
Log.d("MessengerIpcClient", "Received response to request: " + i);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzp.java:40`
```
Log.w("MessengerIpcClient", "Received response for unknown request: " + i);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzp.java:65`
```
Log.v("MessengerIpcClient", "Service connected");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzp.java:96`
```
Log.v("MessengerIpcClient", "Service disconnected");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzp.java:112`
```
Log.d("MessengerIpcClient", "Disconnected: ".concat(String.valueOf(str)));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzp.java:126`
```
Log.v("MessengerIpcClient", "Unbinding service");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzp.java:168`
```
Log.d("MessengerIpcClient", "Sending ".concat(String.valueOf(String.valueOf(zzsVar))));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzp.java:202`
```
Log.w("MessengerIpcClient", "Timing out request: " + i);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzp.java:212`
```
Log.v("MessengerIpcClient", "Finished handling requests, unbinding");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzp.java:236`
```
Log.v("MessengerIpcClient", "Starting bind to GmsCore");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzq.java:23`
```
Log.w("MessengerIpcClient", "Invalid interface descriptor: ".concat(String.valueOf(interfaceDescriptor)));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzs.java:31`
```
Log.d("MessengerIpcClient", "Failing " + toString() + " with " + zztVar.toString());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzs.java:38`
```
Log.d("MessengerIpcClient", "Finishing " + toString() + " with " + String.valueOf(obj));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\cloudmessaging\zzv.java:42`
```
Log.d("MessengerIpcClient", "Queueing ".concat(zzsVar.toString()));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\data\DataHolder.java:122`
```
android.util.Log.d("DataHolder", "Couldn't populate window data for row " + r4 + " - allocating new window.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\images\zaa.java:50`
```
Log.w("ImageManager", "Latch interrupted while posting ".concat(String.valueOf(String.valueOf(this.zab))));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\internal\zac.java:95`
```
Log.e("GoogleApiAvailability", "Network error occurred. Please retry request later.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\internal\zac.java:124`
```
Log.e("GoogleApiAvailability", "The current user profile is restricted and could not use authenticated features.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\internal\zag.java:33`
```
Log.e("DialogRedirect", true == Build.FINGERPRINT.contains("generic") ? "Failed to start resolution intent. This may occur when resolving Google Play services connection issues on emulators with Google APIs but not Google Play Store." : "Failed to start resolution intent.", e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\common\internal\zzf.java:38`
```
Log.w("GmsClient", "service descriptor mismatch: " + this.zzf.getServiceDescriptor() + " vs. " + interfaceDescriptor);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\dynamite\DynamiteModule.java:91`
```
Log.e("DynamiteModule", "Module descriptor id '" + String.valueOf(declaredField.get(null)) + "' didn't match expected id '" + str + "'");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\dynamite\DynamiteModule.java:94`
```
Log.w("DynamiteModule", "Local module descriptor class for " + str + " not found.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\dynamite\DynamiteModule.java:97`
```
Log.e("DynamiteModule", "Failed to load module descriptor class: ".concat(String.valueOf(e.getMessage())));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\auth\zzbz.java:15`
```
Log.e("AUTH", "Error serializing object.", e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\auth\zzcq.java:20`
```
Log.e("PhenotypeClientHelper", String.valueOf(authority).concat(" is an unsupported authority. Only com.google.android.gms.phenotype authority is supported."));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\auth\zzcv.java:19`
```
Log.e("PhenotypeFlag", "Invalid long value for " + this.zzc + ": " + ((String) obj));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\auth\zzi.java:32`
```
Log.w("GoogleAuthSvcClientImpl", "GoogleAuthServiceClientImpl disconnected with reason: ".concat(String.valueOf(str)));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\location\zzaw.java:21`
```
Log.wtf("LocationClientImpl", "onAddGeofenceResult called multiple times", new Exception());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\location\zzaw.java:30`
```
Log.wtf("LocationClientImpl", "Unexpected call to onRemoveGeofencesByRequestIdsResult", new Exception());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\location\zzaw.java:35`
```
Log.wtf("LocationClientImpl", "Unexpected call to onRemoveGeofencesByPendingIntentResult", new Exception());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\location\zzax.java:20`
```
Log.wtf("LocationClientImpl", "onRemoveGeofencesResult called multiple times", new Exception());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\location\zzax.java:29`
```
Log.wtf("LocationClientImpl", "Unexpected call to onAddGeofencesResult", new Exception());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\location\zzaz.java:45`
```
Log.e("LocationClientImpl", "Client disconnected before listeners could be cleaned up", e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\measurement\zzgx.java:24`
```
Log.e("PhenotypeClientHelper", authority + " is an unsupported authority. Only com.google.android.gms.phenotype authority is supported.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\measurement\zzhd.java:23`
```
Log.e("PhenotypeFlag", "Invalid long value for " + super.zzb() + ": " + String.valueOf(obj));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzacv.java:35`
```
Log.w("LocalRequestInterceptor", "Error getting App Check token; using placeholder token instead. Error: " + String.valueOf(appCheckTokenResult.getError()));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzacv.java:39`
```
Log.e("LocalRequestInterceptor", "Unexpected error getting App Check token: " + e.getMessage());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzacw.java:211`
```
Log.e("LocalClient", "Found hermetic configuration for secureToken URL: " + strZza);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzafm.java:49`
```
Log.d(zza, "Failed to read GetTokenResponse from JSONObject");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzafm.java:93`
```
Log.d(zza, "Failed to convert GetTokenResponse to JSON");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzafq.java:71`
```
Log.e("MfaInfo", "Cannot have both MFA phone_info and totp_info");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzafr.java:32`
```
Log.d("JwtToken", "Failed to read JwtToken from JSONObject. " + String.valueOf(e));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\signin\internal\SignInClientImpl.java:100`
```
Log.w("SignInClientImpl", "Remote service probably died when clearAccountFromSessionStore is called");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\bottomsheet\BottomSheetBehavior.java:941`
```
Log.w(TAG, "BottomSheetBehavior now supports multiple callbacks. `setBottomSheetCallback()` removes all existing callbacks, including ones set internally by library authors, which may result in unintended behavior. This may change in the future. Please use `addBottomSheetCallback()` and `removeBottomSheetCallback()` instead to set your own callbacks.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\Chip.java:231`
```
Log.w(TAG, "Do not set the background; Chip manages its own background drawable.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\Chip.java:249`
```
Log.w(TAG, "Chip text must be vertically center and start aligned");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\Chip.java:335`
```
Log.w(TAG, "Chip text must be vertically center and start aligned");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\Chip.java:343`
```
Log.w(TAG, "Do not set the background tint list; Chip manages its own background drawable.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\Chip.java:348`
```
Log.w(TAG, "Do not set the background tint mode; Chip manages its own background drawable.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\Chip.java:353`
```
Log.w(TAG, "Do not set the background color; Chip manages its own background drawable.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\Chip.java:358`
```
Log.w(TAG, "Do not set the background resource; Chip manages its own background drawable.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\Chip.java:364`
```
Log.w(TAG, "Do not set the background; Chip manages its own background drawable.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\Chip.java:373`
```
Log.w(TAG, "Do not set the background drawable; Chip manages its own background drawable.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\color\ColorResourcesLoaderCreator.java:36`
```
Log.w(TAG, "Cannot create memory file descriptor.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\navigation\NavigationBarItemView.java:656`
```
Log.w("NavigationBar", "Multiple badges shouldn't be attached to one item.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\transition\MaterialContainerTransform.java:414`
```
Log.w(TAG, "Skipping due to null start bounds. Ensure start view is laid out and measured.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\transition\MaterialContainerTransform.java:419`
```
Log.w(TAG, "Skipping due to null end bounds. Ensure end view is laid out and measured.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\transition\platform\MaterialContainerTransform.java:414`
```
Log.w(TAG, "Skipping due to null start bounds. Ensure start view is laid out and measured.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\transition\platform\MaterialContainerTransform.java:419`
```
Log.w(TAG, "Skipping due to null end bounds. Ensure end view is laid out and measured.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\play\core\appupdate\internal\zzm.java:61`
```
return Log.w("PlayCore", zzf(this.zza, "Phonesky package is not signed -- possibly self-built package. Could not verify.", objArr));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\play\core\review\internal\zzi.java:61`
```
return Log.w("PlayCore", zzf(this.zza, "Phonesky package is not signed -- possibly self-built package. Could not verify.", objArr));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\play\integrity\internal\q.java:35`
```
return Log.e("PlayCore", e(this.f585a, "Phonesky is not installed.", objArr));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\play\integrity\internal\q.java:56`
```
return Log.w("PlayCore", e(this.f585a, "Phonesky package is not signed -- possibly self-built package. Could not verify.", objArr));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\FirebaseAuth.java:691`
```
Log.e("FirebaseAuth", "Invoking verification failure callback for phone number/uid - " + str);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\FirebaseAuth.java:726`
```
Log.i("FirebaseAuth", "Error parsing URL: '" + str + "', " + e.getMessage());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\FirebaseAuth.java:768`
```
Log.d("FirebaseAuth", "Notifying auth state listeners about a sign-out event.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\FirebaseAuth.java:770`
```
Log.d("FirebaseAuth", "Notifying auth state listeners about user ( " + firebaseUser.getUid() + " ).");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\FirebaseAuth.java:777`
```
Log.d("FirebaseAuth", "Notifying id token listeners about user ( " + firebaseUser.getUid() + " ).");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\FirebaseAuth.java:779`
```
Log.d("FirebaseAuth", "Notifying id token listeners about a sign-out event.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\PhoneMultiFactorInfo.java:64`
```
Log.d("PhoneMultiFactorInfo", "Failed to jsonify this object");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\TotpMultiFactorInfo.java:65`
```
Log.d("TotpMultiFactorInfo", "Failed to jsonify this object");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\GenericIdpActivity.java:102`
```
Log.w("GenericIdpActivity", "Error getting App Check token; using placeholder token instead. Error: " + String.valueOf(appCheckTokenResult.getError()));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\GenericIdpActivity.java:106`
```
Log.e("GenericIdpActivity", "Unexpected error getting App Check token: " + task.getException().getMessage());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\RecaptchaActivity.java:81`
```
Log.w(zzb, "Error getting App Check token; using placeholder token instead. Error: " + String.valueOf(appCheckTokenResult.getError()));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\RecaptchaActivity.java:85`
```
Log.e(zzb, "Unexpected error getting App Check token: " + task.getException().getMessage());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\RecaptchaActivity.java:218`
```
Log.e(zzb, "Failed to find registration for this event - failing to prevent session injection.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zza.java:36`
```
Log.i(str2, "ForceRecaptchaFlow from phoneAuthOptions = " + z2 + ", ForceRecaptchaFlow from firebaseSettings = " + zzzVar.zzc());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zza.java:89`
```
Log.e(zza, "Play Integrity Token fetch failed, falling back to Recaptcha" + (task.getException() == null ? "" : task.getException().getMessage()));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zzaz.java:37`
```
Log.e("FederatedAuthReceiver", "Failed to unregister BroadcastReceiver because the Activity that launched this flow has been garbage collected; please do not finish() your Activity while performing a FederatedAuthProvider operation.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zzbb.java:30`
```
Log.e("FederatedAuthReceiver", "Failed to unregister BroadcastReceiver because the Activity that launched this flow has been garbage collected; please do not finish() your Activity while performing a FederatedAuthProvider operation.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zzbl.java:31`
```
Log.e("RecaptchaCallWrapper", "Failed to get Recaptcha token, error - " + ((Exception) Preconditions.checkNotNull(task.getException())).getMessage() + "\n\n Failing open with a fake token.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zzbq.java:25`
```
Log.i("RecaptchaCallWrapper", "Invalid token - Refreshing Recaptcha Enterprise config and fetching new token for tenant " + this.zza);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zzbw.java:26`
```
Log.i("RecaptchaHandler", "Ignoring error related to fetching recaptcha config - " + exc.getMessage());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zze.java:19`
```
Log.e(zza.zza, String.format("Failed to get reCAPTCHA token with error [%s]- calling backend without app verification", exc.getMessage()));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zzy.java:45`
```
Log.d("DefaultAuthUserInfo", "Failed to unpack UserInfo from JSON");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\internal\zzy.java:92`
```
Log.d("DefaultAuthUserInfo", "Failed to jsonify this object");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzaa.java:26`
```
Log.i("FirebaseAuth", "Logging in as " + this.zza + " with empty reCAPTCHA token");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzaa.java:28`
```
Log.i("FirebaseAuth", "Got reCAPTCHA token for login with email " + this.zza);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzac.java:26`
```
Log.i("FirebaseAuth", " Email link reauth with empty reCAPTCHA token");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzac.java:28`
```
Log.i("FirebaseAuth", "Got reCAPTCHA token for reauth with email link");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzac.java:35`
```
Log.i("FirebaseAuth", "Reauthenticating " + strZzc + " with empty reCAPTCHA token");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzac.java:37`
```
Log.i("FirebaseAuth", "Got reCAPTCHA token for reauth with " + strZzc);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzad.java:25`
```
Log.i("FirebaseAuth", "Email link login/reauth with empty reCAPTCHA token");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzad.java:27`
```
Log.i("FirebaseAuth", "Got reCAPTCHA token for login/reauth with email link");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzk.java:30`
```
Log.e("FirebaseAuth", exception != null ? "Error while validating application identity: " + exception.getMessage() : "Error while validating application identity: ");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzk.java:32`
```
Log.e("FirebaseAuth", "Proceeding without any application identifier.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzl.java:27`
```
Log.e("FirebaseAuth", "Error while validating application identity: " + (exception != null ? exception.getMessage() : ""));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzl.java:29`
```
Log.e("FirebaseAuth", "Proceeding without any application identifier.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzm.java:40`
```
Log.d("FirebaseAuth", "Re-triggering phone verification with Recaptcha flow forced for phone number " + this.zza.zzh());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzm.java:44`
```
Log.d("FirebaseAuth", "Invoking original failure callbacks after phone verification failure for " + this.zza.zzh() + ", error - " + firebaseException.getMessage());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzo.java:19`
```
Log.i("FirebaseAuth", "Creating user with " + this.zza + " with empty reCAPTCHA token");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzo.java:21`
```
Log.i("FirebaseAuth", "Got reCAPTCHA token for sign up with email " + this.zza);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzp.java:22`
```
Log.i("FirebaseAuth", "Linking email account with empty reCAPTCHA token");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzp.java:24`
```
Log.i("FirebaseAuth", "Got reCAPTCHA token for linking email account");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzq.java:18`
```
Log.i("FirebaseAuth", "Email link sign in for " + this.zza + " with empty reCAPTCHA token");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzq.java:20`
```
Log.i("FirebaseAuth", "Got reCAPTCHA token for email link sign in for " + this.zza);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzr.java:18`
```
Log.i("FirebaseAuth", "Password reset request " + this.zza + " with empty reCAPTCHA token");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\auth\zzr.java:20`
```
Log.i("FirebaseAuth", "Got reCAPTCHA token for password reset of email " + this.zza);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\installations\remote\FirebaseInstallationServiceClient.java:275`
```
Log.e(FIS_TAG, "Firebase Installations can not communicate with Firebase server APIs due to invalid configuration. Please update your Firebase initialization process and set valid Firebase options (API key, Project ID, Application ID) when initializing Firebase.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\FirebaseMessaging.java:477`
```
Log.d("FirebaseMessaging", "Invoking onNewToken for app: " + this.firebaseApp.getName());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\GmsRpc.java:146`
```
Log.w("FirebaseMessaging", "FIS auth token is empty");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\GmsRpc.java:151`
```
Log.e("FirebaseMessaging", "Failed to get FIS auth token", e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\MessagingAnalytics.java:99`
```
Log.i(Constants.TAG, "FirebaseApp has not being initialized. Device might be in direct boot mode. Skip exporting delivery metrics to Big Query");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\MessagingAnalytics.java:188`
```
Log.e(Constants.TAG, "Default FirebaseApp has not been initialized. Skip logging event to GA.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\MessagingAnalytics.java:194`
```
Log.e(Constants.TAG, "TransportFactory is null. Skip exporting message delivery metrics to Big Query");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\NotificationParams.java:39`
```
Log.w(Constants.TAG, "notificationCount is invalid: " + integer + ". Skipping setting notificationCount.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\NotificationParams.java:51`
```
Log.w(Constants.TAG, "notificationPriority is invalid " + integer + ". Skipping setting notificationPriority.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\NotificationParams.java:63`
```
Log.w(TAG, "visibility is invalid: " + integer + ". Skipping setting visibility.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\NotificationParams.java:107`
```
Log.w(TAG, "Couldn't parse value of " + userFriendlyKey(str) + "(" + string + ") into a long");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\NotificationParams.java:178`
```
Log.w(TAG, "User defined vibrateTimings is invalid: " + jSONArray + ". Skipping setting vibrateTimings.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\NotificationParams.java:198`
```
Log.w(TAG, "LightSettings is invalid: " + jSONArray + ". " + e.getMessage() + ". Skipping setting LightSettings");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\NotificationParams.java:201`
```
Log.w(TAG, "LightSettings is invalid: " + jSONArray + ". Skipping setting LightSettings");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\ProxyNotificationInitializer.java:60`
```
Log.d(Constants.TAG, "Platform doesn't support proxying.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\ServiceStarter.java:58`
```
Log.d(Constants.TAG, "Restricting intent to a specific service: " + strResolveServiceClassName);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\ServiceStarter.java:99`
```
Log.e(Constants.TAG, "Error resolving target intent service, skipping classname enforcement. Resolved service was: " + serviceInfo.packageName + "/" + serviceInfo.name);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\ServiceStarter.java:102`
```
Log.e(Constants.TAG, "Failed to resolve target intent service, skipping classname enforcement");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\Store.java:102`
```
Log.w(Constants.TAG, "Failed to parse token: " + e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\Store.java:117`
```
Log.w(Constants.TAG, "Failed to encode token: " + e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\SyncTask.java:42`
```
Log.e(Constants.TAG, "Topic sync or token retrieval failed on hard failure exceptions: " + e.getMessage() + ". Won't retry the operation.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\SyncTask.java:84`
```
Log.e(Constants.TAG, "Token retrieval failed: null");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\SyncTask.java:90`
```
Log.d(Constants.TAG, "Token successfully retrieved");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\SyncTask.java:94`
```
Log.w(Constants.TAG, "Token retrieval failed: " + e.getMessage() + ". Will retry token retrieval");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\SyncTask.java:98`
```
Log.w(Constants.TAG, "Token retrieval failed without exception message. Will retry token retrieval");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\SyncTask.java:103`
```
Log.w(Constants.TAG, "Token retrieval failed with SecurityException. Will retry token retrieval");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\messaging\WithinAppServiceConnection.java:55`
```
Log.w(Constants.TAG, "Service took too long to process intent: " + this.intent.getAction() + " finishing.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\remoteconfig\internal\ConfigAutoFetch.java:247`
```
Log.d(FirebaseRemoteConfig.TAG, "Fetched template version is the same as SDK's current version. Retrying fetch.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\remoteconfig\internal\rollouts\RolloutsStateFactory.java:35`
```
Log.w(FirebaseRemoteConfig.TAG, String.format("Rollout has multiple affected parameter keys.Only the first key will be included in RolloutsState. rolloutId: %s, affectedParameterKeys: %s", string, jSONArray));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\EventGDTLogger.java:41`
```
Log.d(TAG, "Session Event: " + strEncode);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\FirebaseSessions.java:42`
```
Log.d(TAG, "Initializing Firebase Sessions SDK.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\FirebaseSessions.java:177`
```
Log.w(FirebaseSessions.TAG, "FirebaseApp instance deleted. Sessions library will stop collecting data.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionDatastoreImpl$firebaseSessionDataFlow$1.java:44`
```
Log.e("FirebaseSessionsRepo", "Error reading stored session data.", (Throwable) this.L$1);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionDatastoreImpl.java:56`
```
Log.w("FirebaseSessionsRepo", "CorruptionException in sessions DataStore in " + ProcessDetailsProvider.INSTANCE.getProcessName$com_google_firebase_firebase_sessions() + '.', ex);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionDatastoreImpl.java:279`
```
Log.w(SessionDatastoreImpl.TAG, "Failed to update session Id: " + e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionFirelogPublisherImpl.java:224`
```
Log.d(TAG, "Successfully logged Session Start event: " + sessionEvent.getSessionData().getSessionId());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionFirelogPublisherImpl.java:226`
```
Log.e(TAG, "Error logging Session Start event to DataTransport: ", e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleClient$ClientUpdateHandler$handleSessionUpdate$1.java:63`
```
Log.d(SessionLifecycleClient.TAG, "Notified " + sessionSubscriber.getSessionSubscriberName() + " of new session " + str);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleClient.java:60`
```
Log.d(SessionLifecycleClient.TAG, "Connected to SessionLifecycleService. Queue size " + this.this$0.queuedMessages.size());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleClient.java:69`
```
Log.d(SessionLifecycleClient.TAG, "Disconnected from SessionLifecycleService");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleClient.java:100`
```
Log.w(SessionLifecycleClient.TAG, "Received unexpected event from the SessionLifecycleService: " + msg);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleClient.java:105`
```
Log.d(SessionLifecycleClient.TAG, "Session update received: " + sessionId);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleClient.java:174`
```
Log.d(SessionLifecycleClient.TAG, "Sessions SDK did not have any dependent SDKs register as dependencies. Events will not be sent.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleClient.java:178`
```
Log.d(SessionLifecycleClient.TAG, "Data Collection is disabled for all subscribers. Skipping this Event");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleClient.java:197`
```
Log.d(SessionLifecycleClient.TAG, "Data Collection is disabled for all subscribers. Skipping this Event");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:60`
```
Log.d(SessionLifecycleService.TAG, "Ignoring old message from " + msg.getWhen() + " which is older than " + this.lastMsgTimeMs + '.');
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:73`
```
Log.w(SessionLifecycleService.TAG, "Received unexpected event from the SessionLifecycleClient: " + msg);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:79`
```
Log.d(SessionLifecycleService.TAG, "Activity foregrounding at " + msg.getWhen() + '.');
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:81`
```
Log.d(SessionLifecycleService.TAG, "Cold start detected.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:85`
```
Log.d(SessionLifecycleService.TAG, "Session too long in background. Creating new session.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:92`
```
Log.d(SessionLifecycleService.TAG, "Activity backgrounding at " + msg.getWhen());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:101`
```
Log.d(SessionLifecycleService.TAG, "Client " + msg.replyTo + " bound at " + msg.getWhen() + ". Clients: " + this.boundClients.size());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:106`
```
Log.d(SessionLifecycleService.TAG, "Generated new session " + SessionGenerator.INSTANCE.getInstance().getCurrentSession().getSessionId());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:112`
```
Log.d(SessionLifecycleService.TAG, "Broadcasting new session: " + SessionGenerator.INSTANCE.getInstance().getCurrentSession());
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:126`
```
Log.d(SessionLifecycleService.TAG, "App has not yet foregrounded. Using previously stored session: " + currentSessionId);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:140`
```
Log.d(SessionLifecycleService.TAG, "Removing dead client from list: " + client);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleService.java:143`
```
Log.w(SessionLifecycleService.TAG, "Unable to push new session to " + client + '.', e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleServiceBinderImpl.java:43`
```
Log.w(TAG, "Failed to bind session lifecycle service to application.", e);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleServiceBinderImpl.java:51`
```
Log.i(TAG, "Session lifecycle service binding failed.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\SessionLifecycleServiceBinderImpl.java:59`
```
return Integer.valueOf(Log.w(TAG, "Session lifecycle service binding failed.", e));
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\api\FirebaseSessionsDependencies.java:50`
```
Log.d(TAG, "Subscriber " + sessionSubscriberName + " already registered.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\api\FirebaseSessionsDependencies.java:54`
```
Log.d(TAG, "Subscriber " + sessionSubscriberName + " registered.");
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_LOG_SENSITIVE (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\sessions\settings\SessionsSettings.java:51`
```
Log.w("SessionsSettings", "CorruptionException in settings DataStore in " + ProcessDetailsProvider.INSTANCE.getProcessName$com_google_firebase_firebase_sessions() + '.', ex);
```
- **Why it matters:** Potential sensitive data in Android log statement.

### ANDROID_WEBVIEW_JS_INTERFACE (medium)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\braze\ui\inappmessage\factories\DefaultInAppMessageHtmlFullViewFactory.java:61`
```
messageWebView.addJavascriptInterface(inAppMessageJavascriptInterface, InAppMessageHtmlBaseView.BRAZE_BRIDGE_PREFIX);
```
- **Why it matters:** WebView addJavascriptInterface detected. On API<17 can lead to RCE; review necessity.

### ANDROID_WEBVIEW_JS_INTERFACE (medium)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\braze\ui\inappmessage\factories\DefaultInAppMessageHtmlViewFactory.java:61`
```
messageWebView.addJavascriptInterface(inAppMessageJavascriptInterface, InAppMessageHtmlBaseView.BRAZE_BRIDGE_PREFIX);
```
- **Why it matters:** WebView addJavascriptInterface detected. On API<17 can lead to RCE; review necessity.

### ANDROID_WEBVIEW_JS_INTERFACE (medium)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\appevents\AppEventsLoggerImpl.java:963`
```
webView.addJavascriptInterface(facebookSDKJSInterface, Intrinsics.stringPlus("fbmq_", FacebookSdk.getApplicationId()));
```
- **Why it matters:** WebView addJavascriptInterface detected. On API<17 can lead to RCE; review necessity.

### ANDROID_WEBVIEW_JS_INTERFACE (medium)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\recaptcha\internal\zzez.java:52`
```
webView.addJavascriptInterface(zzeqVar, "RN");
```
- **Why it matters:** WebView addJavascriptInterface detected. On API<17 can lead to RCE; review necessity.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\Util.java:516`
```
return (new Random().nextDouble() * (d3 - d2)) + d2;
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\core\utilities\EventsFileManager.java:466`
```
file.renameTo(new File(this.directory, nameWithoutExtension + '-' + System.currentTimeMillis() + '-' + new Random().nextInt(1000)));
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\braze\support\IntentUtils.java:63`
```
return new Random();
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\bugfender\sdk\C3012o0.java:450`
```
return new Random().nextInt(i2 - i) + i;
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\bugfender\sdk\d1.java:65`
```
private final Random b = new Random();
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\FacebookException.java:22`
```
Random random = new Random();
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\facebook\internal\Utility.java:1317`
```
String string = new BigInteger(length * 5, new Random()).toString(32);
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\common\cache\Striped64.java:24`
```
static final Random rng = new Random();
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\common\hash\Striped64.java:24`
```
static final Random rng = new Random();
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\remoteconfig\RemoteConfigComponent.java:58`
```
private static final Random DEFAULT_RANDOM = new Random();
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\remoteconfig\internal\ConfigAutoFetch.java:32`
```
private final Random random = new Random();
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\firebase\remoteconfig\internal\ConfigRealtimeHttpClient.java:68`
```
private final Random random = new Random();
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### CRYPTO_INSECURE_RANDOM (medium)
- **Category:** crypto
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\gson\internal\StringMap.java:23`
```
private static final int seed = new Random().nextInt();
```
- **Why it matters:** Weak or misused crypto pattern: CRYPTO_INSECURE_RANDOM.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\impl\appupdate\ForceUpdateErrorDialog.java:44`
```
return new Intent("android.intent.action.VIEW", Uri.parse("http://play.google.com/store/apps/details?id=com.adhoclabs.burner"));
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzaen.java:11`
```
private String zzb = "http://localhost";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\internal\p002firebaseauthapi\zzags.java:110`
```
this.zza = "http://localhost";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\Chip.java:55`
```
private static final String NAMESPACE_ANDROID = "http://schemas.android.com/apk/res/android";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\chip\ChipDrawable.java:50`
```
private static final String NAMESPACE_APP = "http://schemas.android.com/apk/res-auto";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\material\search\SearchBar.java:48`
```
private static final String NAMESPACE_APP = "http://schemas.android.com/apk/res-auto";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\zxing\client\result\URIParsedResult.java:40`
```
return (iIndexOf < 0 || isColonFollowedByPortNumber(strTrim, iIndexOf)) ? "http://".concat(String.valueOf(strTrim)) : strTrim;
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\remote\b.java:21`
```
private static final String d = "\n            {\n                \"id\":\"52b467e9e4b0a3b4e5ec644c\",\n                \"name\":\"Manage multiple Docs sites\",\n                \"text\":\"<html><body><p> You might want to create different Docs ss.&nbsp</p></body></html>\",\n                \"related\":[\n                    {\n                        \"id\":\"524db929e4b0c2199a391f39\",\n                        \"name\":\"Email commands \",\n                        \"url\":\"http://docs.helpscout.net/article/43-email-commands\"\n                    },\n                    {\n                        \"id\":\"52b5b007e4b0a3b4e5ec64da\",\n                        \"name\":\"How mailboxes work in Help Scout\",\n                        \"url\":\"http://docs.helpscout.net/article/231-mailboxes\"\n                    }\n                ],\n                \"url\":\"http://docs.helpscout.net/article/229-multiple-docs-sites\"\n            }\n        ";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\remote\b.java:21`
```
private static final String d = "\n            {\n                \"id\":\"52b467e9e4b0a3b4e5ec644c\",\n                \"name\":\"Manage multiple Docs sites\",\n                \"text\":\"<html><body><p> You might want to create different Docs ss.&nbsp</p></body></html>\",\n                \"related\":[\n                    {\n                        \"id\":\"524db929e4b0c2199a391f39\",\n                        \"name\":\"Email commands \",\n                        \"url\":\"http://docs.helpscout.net/article/43-email-commands\"\n                    },\n                    {\n                        \"id\":\"52b5b007e4b0a3b4e5ec64da\",\n                        \"name\":\"How mailboxes work in Help Scout\",\n                        \"url\":\"http://docs.helpscout.net/article/231-mailboxes\"\n                    }\n                ],\n                \"url\":\"http://docs.helpscout.net/article/229-multiple-docs-sites\"\n            }\n        ";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\remote\b.java:21`
```
private static final String d = "\n            {\n                \"id\":\"52b467e9e4b0a3b4e5ec644c\",\n                \"name\":\"Manage multiple Docs sites\",\n                \"text\":\"<html><body><p> You might want to create different Docs ss.&nbsp</p></body></html>\",\n                \"related\":[\n                    {\n                        \"id\":\"524db929e4b0c2199a391f39\",\n                        \"name\":\"Email commands \",\n                        \"url\":\"http://docs.helpscout.net/article/43-email-commands\"\n                    },\n                    {\n                        \"id\":\"52b5b007e4b0a3b4e5ec64da\",\n                        \"name\":\"How mailboxes work in Help Scout\",\n                        \"url\":\"http://docs.helpscout.net/article/231-mailboxes\"\n                    }\n                ],\n                \"url\":\"http://docs.helpscout.net/article/229-multiple-docs-sites\"\n            }\n        ";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\remote\b.java:22`
```
private static final String e = "\n            {\"items\":[{\"type\":\"article\",\"suggestion\":{\"id\":\"54f0a3e8e4b086c0c096a1de\",\"name\":\"Mock working with variables\",\"url\":\"http://docs.brightwurks.com/article/468-variables\"}},{\"type\":\"article\",\"suggestion\":{\"id\":\"525552b4e4b0fc33a10a7ca1\",\"name\":\"Forward from Outlook.com and Office365\",\"url\":\"http://docs.brightwurks.com/article/76-office-outlook-forwarding\"}},{\"type\":\"article\",\"suggestion\":{\"id\":\"525216e7e4b00055e61de9d4\",\"name\":\"Enable and respond to email notifications\",\"url\":\"http://docs.brightwurks.com/article/67-email-notifications\"}},{\"type\":\"link\",\"suggestion\":{\"url\":\"http://helpscout.com\",\"text\":\"Help Scout\"}},{\"type\":\"link\",\"suggestion\":{\"url\":\"http://bbc.co.uk\",\"text\":\"BBC News\"}}]}\n        ";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\remote\b.java:22`
```
private static final String e = "\n            {\"items\":[{\"type\":\"article\",\"suggestion\":{\"id\":\"54f0a3e8e4b086c0c096a1de\",\"name\":\"Mock working with variables\",\"url\":\"http://docs.brightwurks.com/article/468-variables\"}},{\"type\":\"article\",\"suggestion\":{\"id\":\"525552b4e4b0fc33a10a7ca1\",\"name\":\"Forward from Outlook.com and Office365\",\"url\":\"http://docs.brightwurks.com/article/76-office-outlook-forwarding\"}},{\"type\":\"article\",\"suggestion\":{\"id\":\"525216e7e4b00055e61de9d4\",\"name\":\"Enable and respond to email notifications\",\"url\":\"http://docs.brightwurks.com/article/67-email-notifications\"}},{\"type\":\"link\",\"suggestion\":{\"url\":\"http://helpscout.com\",\"text\":\"Help Scout\"}},{\"type\":\"link\",\"suggestion\":{\"url\":\"http://bbc.co.uk\",\"text\":\"BBC News\"}}]}\n        ";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\remote\b.java:22`
```
private static final String e = "\n            {\"items\":[{\"type\":\"article\",\"suggestion\":{\"id\":\"54f0a3e8e4b086c0c096a1de\",\"name\":\"Mock working with variables\",\"url\":\"http://docs.brightwurks.com/article/468-variables\"}},{\"type\":\"article\",\"suggestion\":{\"id\":\"525552b4e4b0fc33a10a7ca1\",\"name\":\"Forward from Outlook.com and Office365\",\"url\":\"http://docs.brightwurks.com/article/76-office-outlook-forwarding\"}},{\"type\":\"article\",\"suggestion\":{\"id\":\"525216e7e4b00055e61de9d4\",\"name\":\"Enable and respond to email notifications\",\"url\":\"http://docs.brightwurks.com/article/67-email-notifications\"}},{\"type\":\"link\",\"suggestion\":{\"url\":\"http://helpscout.com\",\"text\":\"Help Scout\"}},{\"type\":\"link\",\"suggestion\":{\"url\":\"http://bbc.co.uk\",\"text\":\"BBC News\"}}]}\n        ";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\remote\b.java:22`
```
private static final String e = "\n            {\"items\":[{\"type\":\"article\",\"suggestion\":{\"id\":\"54f0a3e8e4b086c0c096a1de\",\"name\":\"Mock working with variables\",\"url\":\"http://docs.brightwurks.com/article/468-variables\"}},{\"type\":\"article\",\"suggestion\":{\"id\":\"525552b4e4b0fc33a10a7ca1\",\"name\":\"Forward from Outlook.com and Office365\",\"url\":\"http://docs.brightwurks.com/article/76-office-outlook-forwarding\"}},{\"type\":\"article\",\"suggestion\":{\"id\":\"525216e7e4b00055e61de9d4\",\"name\":\"Enable and respond to email notifications\",\"url\":\"http://docs.brightwurks.com/article/67-email-notifications\"}},{\"type\":\"link\",\"suggestion\":{\"url\":\"http://helpscout.com\",\"text\":\"Help Scout\"}},{\"type\":\"link\",\"suggestion\":{\"url\":\"http://bbc.co.uk\",\"text\":\"BBC News\"}}]}\n        ";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\remote\b.java:22`
```
private static final String e = "\n            {\"items\":[{\"type\":\"article\",\"suggestion\":{\"id\":\"54f0a3e8e4b086c0c096a1de\",\"name\":\"Mock working with variables\",\"url\":\"http://docs.brightwurks.com/article/468-variables\"}},{\"type\":\"article\",\"suggestion\":{\"id\":\"525552b4e4b0fc33a10a7ca1\",\"name\":\"Forward from Outlook.com and Office365\",\"url\":\"http://docs.brightwurks.com/article/76-office-outlook-forwarding\"}},{\"type\":\"article\",\"suggestion\":{\"id\":\"525216e7e4b00055e61de9d4\",\"name\":\"Enable and respond to email notifications\",\"url\":\"http://docs.brightwurks.com/article/67-email-notifications\"}},{\"type\":\"link\",\"suggestion\":{\"url\":\"http://helpscout.com\",\"text\":\"Help Scout\"}},{\"type\":\"link\",\"suggestion\":{\"url\":\"http://bbc.co.uk\",\"text\":\"BBC News\"}}]}\n        ";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\remote\b.java:23`
```
private static final String f = "\n        {\n           \"items\":[\n              {\n                 \"id\":\"524db929e4b0c2199a391f39\",\n                 \"name\":\"Mock Email commands \",\n                 \"preview\":\"Email commands allow you to update Help Scout conversations via your email client...\",\n                 \"url\":\"http://docs.helpscout.net/article/43-email-commands\"\n              },\n              {\n                 \"id\":\"52b5b007e4b0a3b4e5ec64da\",\n                 \"name\":\"Mock How mailboxes work in Help Scout\",\n                 \"preview\":\"A mailbox in Help Scout is like any other inbox: it holds email. Your support team will work ...\",\n                 \"url\":\"http://docs.helpscout.net/article/231-mailboxes\"\n              }\n           ],\n           \"paging\" : {\n              \"page\" : 1,\n              \"pages\" : 4,\n              \"pageSize\" : 20,\n              \"count\" : 75\n           }\n        }\n        ";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\remote\b.java:23`
```
private static final String f = "\n        {\n           \"items\":[\n              {\n                 \"id\":\"524db929e4b0c2199a391f39\",\n                 \"name\":\"Mock Email commands \",\n                 \"preview\":\"Email commands allow you to update Help Scout conversations via your email client...\",\n                 \"url\":\"http://docs.helpscout.net/article/43-email-commands\"\n              },\n              {\n                 \"id\":\"52b5b007e4b0a3b4e5ec64da\",\n                 \"name\":\"Mock How mailboxes work in Help Scout\",\n                 \"preview\":\"A mailbox in Help Scout is like any other inbox: it holds email. Your support team will work ...\",\n                 \"url\":\"http://docs.helpscout.net/article/231-mailboxes\"\n              }\n           ],\n           \"paging\" : {\n              \"page\" : 1,\n              \"pages\" : 4,\n              \"pageSize\" : 20,\n              \"count\" : 75\n           }\n        }\n        ";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\pusher\client\example\PresenceChannelExampleApp.java:18`
```
private String authorizationEndpoint = "http://localhost:3030/pusher/auth";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\pusher\client\example\PrivateChannelExampleApp.java:15`
```
private String authorizationEndpoint = "http://localhost:3030/pusher/auth";
```
- **Why it matters:** Non-TLS HTTP URL found.

### GENERIC_HTTP_URL (medium)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\pusher\client\example\PrivateEncryptedChannelExampleApp.java:15`
```
private String authorizationEndpoint = "http://localhost:3030/pusher/auth";
```
- **Why it matters:** Non-TLS HTTP URL found.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\BurnerApplication_HiltComponents.java:296`
```
import com.adhoclabs.burner.features.infra.clipboard.di.HiltWrapper_ClipboardManagerModule;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\BurnerApplication_HiltComponents.java:707`
```
@Component(modules = {ActiveStandardSubscriptionQuery.Binding.class, ActiveVerifiedSubscriptionIdLiveQuery.Binding.class, ActiveVerifiedSubscriptionQuery.Binding.class, AdjustAnalyticsModule.class, AmplitudeAnalyticsInitializer.Binding.class, AmplitudeAnalyticsSubscriber.Binding.class, AmplitudeFeatureFlagInitializer.Binding.class, AnalyticsReporterModule.Binding.class, ApplicationContextModule.class, ApplicationCoroutineScope.Binding.class, AuthLeversModule.class, AuthModule.class, com.adhoclabs.burner.infra.network.di.AuthModule.class, AvailableNumberViewModelToAvailableNumberAdapterItemMapper.Binding.class, BillingClientEitherBinding.class, BugfenderLogger.Binding.class, BurnerAppAnalyticsImpl.Binding.class, ActivityRetainedCBuilderModule.class, ServiceCBuilderModule.class, BurnerCommonModule.class, BurnerSerializationModule.class, CarrierValidationFeatureFlag.Binding.class, ChuckerModule.class, ClientFeaturesModule.class, ColorMapModule.class, ColorUtilModule.class, ConnectivityManagerModule.class, ContactsUtilModule.class, CreateBurnerMutation.Binding.class, CreateBurnerRetrofit.Binding.class, CreateBurnerRetrofitRpc.Binding.class, DatabaseModule.class, DeleteAllConversationsStatement.Binding.class, DeleteAllSubscriptionsStatement.Binding.class, EndOngoingVoipCallWorker_HiltModule.class, ExtendBurnerModule.class, FacebookModule.class, FirebaseFeatureFlagMap.Binding.class, ForceUpdateModule.class, GetAccountSettingsImpl.Binding.class, GetAccountSettingsRetrofit.Binding.class, GetAreaCodeSuggestionListQuery.Binding.class, GetAreaCodeSuggestionListRetrofitRpc.Binding.class, GetAvailableBurnerListQuery.Binding.class, GetAvailableBurnerListRetrofit.Binding.class, GetAvailableBurnerListRetrofitRpc.Binding.class, GetBurnerModule.class, GetCreditProductListRetrofit.Binding.class, GetCreditProductListRetrofitRpc.Binding.class, GetExtensionProductsForBurnerModule.class, GetNetworkConnectionTypeImpl.Binding.class, GetPrepaidBurnerSkuQuery.Binding.class, GetPrepaidProductListRetrofit.Binding.class, GetPrepaidProductListRetrofitRpc.Binding.class, GetSkuCompatibleSubscriptionImpl.Binding.class, GetStandardBurnerListImpl.Binding.class, GetSubscriptionManagementProductListImpl.Binding.class, GetSubscriptionManagementSkuListRetrofitRpc.Binding.class, GetSubscriptionProductListRetrofit.Binding.class, GetSubscriptionProductListRetrofitRpc.Binding.class, GetSubscriptionProductRetrofit.Binding.class, GetSubscriptionProductRetrofitRpc.Binding.class, GetSubscriptionsQuery.Binding.class, GetSubscriptionsRetrofit.Binding.class, GetSuggestedAreaCodeListRetrofit.Binding.class, GetUserRetrofit.Binding.class, GetUserRetrofitRpc.Binding.class, GetUserSsoAccountFirebase.Binding.class, GetUserSubscriptionListRetrofit.Binding.class, GetUserSubscriptionListRetrofitRpc.Binding.class, GetUserSubscriptionProductListRetrofit.Binding.class, HasPasscodeEnabledImpl.Binding.class, HiltWrapper_AcknowledgeModule.class, HiltWrapper_ActiveCallHelperModule.class, HiltWrapper_ActivityNavigationModule.class, HiltWrapper_AdjustApplicationModule.class, HiltWrapper_AdjustAttributionListenerModule.class, HiltWrapper_AdjustModule.class, HiltWrapper_AmplitudeLevers_Binding.class, HiltWrapper_AnalyticsReporterModule.class, HiltWrapper_ApiModule.class, HiltWrapper_AppMigrationModule.class, HiltWrapper_AppShimsModule.class, HiltWrapper_ApplicationCacheModule.class, HiltWrapper_ApplicationEmittersModule.class, HiltWrapper_ApplicationModule.class, com.adhoclabs.burner.di.HiltWrapper_AuthenticationModule.class, HiltWrapper_AuthenticationNavigationModule.class, HiltWrapper_BeaconModule.class, HiltWrapper_BillingManagerModule.class, HiltWrapper_BrazeApplicationModule.class, HiltWrapper_BrazeModule.class, HiltWrapper_BurnerCreationAnalyticsReporterModule.class, HiltWrapper_BurnerNumberRepositoryModule.class, HiltWrapper_BurnerRetrofitModule.class, HiltWrapper_BurnerSelectionNavigationModule.class, HiltWrapper_BurnerUseCaseModule.class, HiltWrapper_BurnerVoicemailSettingAnalyticsReporterModule.class, HiltWrapper_BurnersDataSourceInternalModule.class, HiltWrapper_BurnersDataSourceModule.class, HiltWrapper_BurnersRepositoryInternalModule.class, HiltWrapper_BurnersRepositoryModule.class, HiltWrapper_CallAnalyticsReporterModule.class, HiltWrapper_CallModule.class, HiltWrapper_CallRepositoryInternalModule.class, HiltWrapper_CallRepositoryModule.class, com.adhoclabs.burner.infra.repositories.call.voip.di.HiltWrapper_CallRepositoryModule.class, HiltWrapper_CallRepositoryWorkersModule.class, HiltWrapper_ClearAmplitudeFeatureFlags.class, HiltWrapper_ClientFeaturesRepositoryModule.class, HiltWrapper_ClientRetrofitModule.class, HiltWrapper_ClipboardManagerModule.class, HiltWrapper_ComposeGroupNavigationModule.class, HiltWrapper_ContactLineSelectorCoreModule.class, HiltWrapper_ContactsDataSourceInternalModule.class, HiltWrapper_ContactsDataSourceModule.class, HiltWrapper_ContactsRepositoryInternalModule.class, HiltWrapper_ContactsRepositoryModule.class, HiltWrapper_CreatePasscodeNavigationModule.class, HiltWrapper_CreatorModule.class, HiltWrapper_CreditsAnalyticsReporterModule.class, HiltWrapper_CreditsDataSourceInternalModule.class, HiltWrapper_CreditsDataSourceModule.class, HiltWrapper_CreditsRepositoryInternalModule.class, HiltWrapper_CreditsRepositoryModule.class, HiltWrapper_DataSourceCommonModule.class, HiltWrapper_DataStoreModule.class, HiltWrapper_DatabaseModule.class, HiltWrapper_DatabaseQueryModule.class, HiltWrapper_DatabaseTablesModule.class, HiltWrapper_DeviceContactsModule.class, HiltWrapper_DialerAnalyticsReporterModule.class, HiltWrapper_DispatchersModule.class, HiltWrapper_DynamicDependencyModule.class, HiltWrapper_ExpirationSheetModule.class, HiltWrapper_FcmRegistrationDataSourceInternalModule.class, HiltWrapper_FcmRegistrationDataSourceModule.class, HiltWrapper_FeatureGroupNavigatorInitializerModule.class, HiltWrapper_FileModule.class, HiltWrapper_FirebaseAuthAnalyticsReporterModule.class, HiltWrapper_FirebaseLoggerModule.class, HiltWrapper_FirebaseModule.class, HiltWrapper_FirstCallDataSourceInternalModule.class, HiltWrapper_FirstCallDataSourceModule.class, HiltWrapper_FragmentGetContextFix_FragmentGetContextFixModule.class, HiltWrapper_GetGooglePlaySubscriptionPricingListBinding.class, HiltWrapper_GetProductPricingListRpcBinding.class, HiltWrapper_GooglePlayModule.class, HiltWrapper_HomeNavigationModule.class, HiltWrapper_ImageCaptureModule.class, HiltWrapper_ImageCommonModule.class, HiltWrapper_ImageLoaderModule.class, HiltWrapper_ImagePickerModule.class, HiltWrapper_InboxAnalyticsReporterModule.class, HiltWrapper_LeversModule.class, HiltWrapper_LoggerModule.class, HiltWrapper_LoggersModule.class, HiltWrapper_MessagesDataSourceInternalModule.class, HiltWrapper_MessagesDataSourceModule.class, HiltWrapper_MessagesHilt.class, HiltWrapper_MessagesRepositoryInternalModule.class, HiltWrapper_MessagesRepositoryModule.class, HiltWrapper_MessagingAnalyticsReporterModule.class, HiltWrapper_MessagingGroupNavigationModule.class, com.adhoclabs.burner.feature.groups.messaging.di.HiltWrapper_MessagingGroupNavigationModule.class, HiltWrapper_NavigationModule.class, HiltWrapper_NetworkBurnerNumberModule.class, HiltWrapper_NetworkBurnersModule.class, HiltWrapper_NetworkClientModule.class, HiltWrapper_NetworkConfigModule.class, HiltWrapper_NetworkContactsModule.class, HiltWrapper_NetworkInterceptorModule.class, HiltWrapper_NetworkMessagesModule.class, HiltWrapper_NetworkRegistrationModule.class, HiltWrapper_NetworkRetrofitModule.class, HiltWrapper_NetworkRulesModule.class, HiltWrapper_NetworkSettingsModule.class, HiltWrapper_NetworkSubscriptionsModule.class, HiltWrapper_NetworkTelephonyModule.class, HiltWrapper_NetworkUserModule.class, HiltWrapper_NetworkVerificationModule.class, HiltWrapper_NotificationModule.class, HiltWrapper_NotificationsModule.class, HiltWrapper_OnboardingAnalyticsReporterModule.class, HiltWrapper_OnboardingBurnerSelectionNavigationModule.class, HiltWrapper_OnboardingNavigationModule.class, HiltWrapper_PagingModule.class, HiltWrapper_PasscodeDataSourceInternalModule.class, HiltWrapper_PasscodeDataSourceModule.class, HiltWrapper_PasscodeRepositoryInternalModule.class, HiltWrapper_PasscodeRepositoryModule.class, HiltWrapper_PermissionCallPhoneModule.class, HiltWrapper_PermissionDeviceContactsModule.class, HiltWrapper_PermissionImageCaptureModule.class, HiltWrapper_PermissionImagePickModule.class, HiltWrapper_PermissionPostNotificationsModule.class, HiltWrapper_PermissionRecordAudioModule.class, HiltWrapper_PermissionsModule.class, HiltWrapper_PriceModule.class, HiltWrapper_ProductsNetworkServiceModule.class, HiltWrapper_ProviderModule.class, HiltWrapper_RegistrationDataSourceInternalModule.class, HiltWrapper_RegistrationDataSourceModule.class, HiltWrapper_RegistrationRepositoryInternalModule.class, HiltWrapper_RegistrationRepositoryModule.class, HiltWrapper_RouterModule.class, HiltWrapper_RulesDataSourceInternalModule.class, HiltWrapper_RulesDataSourceModule.class, HiltWrapper_RulesRepositoryInternalModule.class, HiltWrapper_RulesRepositoryModule.class, HiltWrapper_ScopesModule.class, HiltWrapper_SelectedLineDataSourceInternalModule.class, HiltWrapper_SelectedLineDataSourceModule.class, HiltWrapper_SelectedLineRepositoryInternalModule.class, HiltWrapper_SelectedLineRepositoryModule.class, HiltWrapper_SerializationInternalModule.class, HiltWrapper_SerializationModule.class, HiltWrapper_SessionAnalyticsReporterModule.class, HiltWrapper_SettingsAnalyticsReporterModule.class, HiltWrapper_SettingsDataSourceInternalModule.class, HiltWrapper_SettingsDataSourceModule.class, HiltWrapper_SettingsNavigationModule.class, HiltWrapper_SettingsRepositoryInternalModule.class, HiltWrapper_SettingsRepositoryModule.class, HiltWrapper_SipRegistrationDataSourceInternalModule.class, HiltWrapper_SipRegistrationDataSourceModule.class, HiltWrapper_SipRegistrationRepositoryInternalModule.class, HiltWrapper_SipRegistrationRepositoryModule.class, HiltWrapper_SubscriptionsDataSourceInternalModule.class, HiltWrapper_SubscriptionsDataSourceModule.class, HiltWrapper_SubscriptionsRepositoryInternalModule.class, HiltWrapper_SubscriptionsRepositoryModule.class, HiltWrapper_SystemThemeBurnerRepositoryModule.class, HiltWrapper_SystemUIModule.class, HiltWrapper_TelephonyModule.class, HiltWrapper_TimeUtilModule.class, HiltWrapper_UserDataSourceInternalModule.class, HiltWrapper_UserDataSourceModule.class, HiltWrapper_UserModule.class, com.adhoclabs.burner.infra.user.di.HiltWrapper_UserModule.class, HiltWrapper_UserPropertiesModule.class, HiltWrapper_UserRepositoryInternalModule.class, HiltWrapper_UserRepositoryModule.class, HiltWrapper_VerificationRepositoryModule.class, HiltWrapper_WorkerFactoryModule.class, HiltWrapper_WorkerModule.class, InitializeAppDataImpl.Binding.class, InitializedFirebaseRemoteConfig.Binding.class, IsFixToolbarSetTitleEnabledFeatureFlag.Binding.class, IsFixToolbarShowEnabledFeatureFlag.Binding.class, LapsedSubscriptionListFlowQuery.Binding.class, LeakCanaryModule.class, LogoutModule.class, ManageVerifiedSubscriptionActionsImpl.Binding.class, NetworkFirebaseModule.class, PhoneNumberFormatBinding.class, PremiumFeatureFlag.Binding.class, ProcessBurnerPushNotification_HiltModule.class, ProcessGeneralPushNotification_HiltModule.class, ProcessSubscriptionPushNotification_HiltModule.class, PurchaseSubscription.Binding.class, PurchaseVerifiedSubscriptionImpl.Binding.class, RejectIncomingVoipCallWorker_HiltModule.class, ReviewModule.class, SerializationModule.class, SetDoNotDisturbImpl.Binding.class, SetDoNotDisturbRetrofit.Binding.class, ShortcodeValidatorModule.class, SqlDelightInsertSubscriptionListResponse.Binding.class, SqlDriverModule.class, SubscriptionManagementLocalDatasourceModule.class, SubscriptionManagementRemoteDatasourceModule.class, SubscriptionManagementRepositoryModule.class, UserIdProviderModule.class, VerifiedNumberLeverFeatureFlag.Binding.class, VerifiedNumberLeversModule.class, VerifiedSubscriptionCompatProviderImpl.Binding.class, VoipRegistrationWorker_HiltModule.class})
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\DaggerBurnerApplication_HiltComponents_SingletonC.java:8`
```
import android.content.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\DaggerBurnerApplication_HiltComponents_SingletonC.java:801`
```
import com.adhoclabs.burner.features.infra.clipboard.di.ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\DaggerBurnerApplication_HiltComponents_SingletonC.java:802`
```
import com.adhoclabs.burner.features.infra.clipboard.impl.ClipboardManagerImpl;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\DaggerBurnerApplication_HiltComponents_SingletonC.java:8057`
```
private ClipboardManager clipboardManager() {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\DaggerBurnerApplication_HiltComponents_SingletonC.java:8058`
```
return ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory.provideAndroidClipboardManager(ApplicationContextModule_ProvideContextFactory.provideContext(this.applicationContextModule));
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\DaggerBurnerApplication_HiltComponents_SingletonC.java:8062`
```
public ClipboardManagerImpl clipboardManagerImpl() {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\DaggerBurnerApplication_HiltComponents_SingletonC.java:8063`
```
return new ClipboardManagerImpl(clipboardManager());
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\feature\groups\messaging\di\MessagingGroupMessagingModule.java:11`
```
import com.adhoclabs.burner.features.infra.clipboard.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\feature\groups\messaging\di\MessagingGroupMessagingModule.java:68`
```
@Metadata(d1 = {"\u0000ô\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u0003J_\u0010\u0004\u001a\b\u0012\u0004\u0012\u00020\u00060\u00052\u0006\u0010\u0007\u001a\u00020\b2\u0006\u0010\t\u001a\u00020\n2\u0011\u0010\u000b\u001a\r\u0012\t\u0012\u00070\u0006¢\u0006\u0002\b\f0\u00052\u0006\u0010\r\u001a\u00020\u000e2\b\b\u0001\u0010\u000f\u001a\u00020\u00102\u000e\b\u0001\u0010\u0011\u001a\b\u0012\u0004\u0012\u00020\u00130\u00122\n\u0010\u0014\u001a\u00060\u0015j\u0002`\u0016H\u0007J\u0012\u0010\u0017\u001a\u00020\u00182\b\b\u0001\u0010\u0019\u001a\u00020\u001aH\u0007JØ\u0001\u0010\u001b\u001a\u00020\u001c2\u0006\u0010\u001d\u001a\u00020\u001e2\b\b\u0001\u0010\u001f\u001a\u00020\u001a2\u0006\u0010 \u001a\u00020!2\b\b\u0001\u0010\u000f\u001a\u00020\u00102\b\b\u0001\u0010\"\u001a\u00020#2\b\b\u0001\u0010$\u001a\u00020\u00102\u0006\u0010%\u001a\u00020&2\b\b\u0001\u0010'\u001a\u00020\u00182\u0012\u0010(\u001a\u000e\u0012\u0004\u0012\u00020*\u0012\u0004\u0012\u00020+0)2\u0012\u0010,\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020+0.0-2\u0006\u0010/\u001a\u0002002\n\u00101\u001a\u00060\u0015j\u0002`\u00162\u0012\u00102\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020504032\u0012\u00106\u001a\u000e\u0012\u0004\u0012\u000208\u0012\u0004\u0012\u000205072\b\b\u0001\u00109\u001a\u00020:2\u000e\u0010;\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010<0\u00122\u0006\u0010=\u001a\u00020>H\u0007J\u0088\u0001\u0010?\u001a\u00020@2\b\b\u0001\u0010A\u001a\u00020\u001c2\u0012\u0010,\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020B0.0-2\u0012\u0010C\u001a\u000e\u0012\u0004\u0012\u00020D\u0012\u0004\u0012\u0002050)2\u0012\u0010E\u001a\u000e\u0012\u0004\u0012\u00020F\u0012\u0004\u0012\u00020G0)2\u0012\u0010H\u001a\u000e\u0012\u0004\u0012\u00020I\u0012\u0004\u0012\u00020J0)2\u0014\u0010K\u001a\u0010\u0012\u0004\u0012\u000205\u0012\u0006\u0012\u0004\u0018\u00010L0)2\u0006\u0010\r\u001a\u00020\u000e2\u0006\u0010M\u001a\u00020NH\u0007¨\u0006O"}, d2 = {"Lcom/adhoclabs/burner/feature/groups/messaging/di/MessagingGroupMessagingModule$Companion;", "", MethodDescription.CONSTRUCTOR_INTERNAL_NAME, "()V", "provideMessagingHydrator", "Lcom/adhoclabs/burner/infra/emitter/Emitter;", "Landroidx/fragment/app/Fragment;", "messagesRepository", "Lcom/adhoclabs/burner/infra/repositories/messages/MessagesRepositoryMutator;", "burnersRepository", "Lcom/adhoclabs/burner/infra/repositories/burners/BurnersRepositoryObserver;", MethodDelegation.ImplementationDelegate.FIELD_NAME_PREFIX, "Lkotlin/jvm/JvmSuppressWildcards;", StepData.ARGS, "Lcom/adhoclabs/burner/feature/groups/messaging/models/MessagingGroupArgs;", "dispatcher", "Lkotlinx/coroutines/CoroutineDispatcher;", "onSetMessagingAttachmentToRetrieve", "Lcom/adhoclabs/burner/infra/usecase/UseCaseMutator;", "Lcom/adhoclabs/burner/features/messaging/common/MessagingAttachmentType;", "logger", "Lco/adhoclabs/burner/core/logging/Logger;", "Lcom/adhoclabs/burner/infra/logger/Logger;", "provideMessagingRouter", "Lcom/adhoclabs/burner/features/messaging/MessagingContract$Router;", "shim", "Lcom/adhoclabs/burner/features/messaging/MessagingShim;", "provideMessagingInteractor", "Lcom/adhoclabs/burner/features/messaging/MessagingContract$Interactor;", "analytics", "Lcom/adhoclabs/burner/infra/analytics/MessagingAnalyticsReporter;", "messagingShim", "clipboardManager", "Lcom/adhoclabs/burner/features/infra/clipboard/ClipboardManager;", "scope", "Lkotlinx/coroutines/CoroutineScope;", "uiDispatcher", "repository", "Lcom/adhoclabs/burner/features/messaging/MessagingContract$Repository;", "router", "getMessagesResultToMessagingDataModel", "Lcom/adhoclabs/burner/infra/mapper/Mapper;", "Lcom/adhoclabs/burner/features/messaging/models/GetMessagesResult;", "Lcom/adhoclabs/burner/features/messaging/impl/MessagingDataModel;", "initialState", "Lkotlinx/coroutines/flow/MutableStateFlow;", "Lcom/adhoclabs/burner/features/infra/state/ContentState;", "phoneUtil", "Lcom/adhoclabs/burner/infra/utils/phone/PhoneUtil;", "log", "failedMessages", "Lcom/adhoclabs/burner/infra/storage/cache/Cache;", "", "Lcom/adhoclabs/burner/features/messaging/models/MessagingMessageDataModel;", "localMessageCreator", "Lcom/adhoclabs/burner/infra/creator/BlockingCreator;", "Lcom/adhoclabs/burner/features/messaging/impl/LocalMessageCreator$Input;", "audioMediaManager", "Lcom/adhoclabs/burner/features/infra/audio/AudioMediaManager;", "setPreparedMedia", "Lcom/adhoclabs/burner/features/infra/audio/AudioMediaManager$Media;", "contactsRepository", "Lcom/adhoclabs/burner/infra/repositories/contacts/ContactsRepository;", "provideViewModelFactory", "Landroidx/lifecycle/ViewModelProvider$Factory;", "interactor", "Lcom/adhoclabs/burner/features/messaging/MessagingContract$DataModel;", "messagingMessageViewModelToMessageDataModel", "Lcom/adhoclabs/burner/features/messaging/mappers/MessagingMessageViewModelToMessageDataModelMapper$Input;", "messagingViewModelDeleteActionToInteractorDeleteAction", "Lcom/adhoclabs/burner/features/messaging/mappers/MessagingViewModelDeleteActionToInteractorDeleteActionMapper$Input;", "Lcom/adhoclabs/burner/features/messaging/MessagingContract$Interactor$DeleteAction;", "messagingContactDataModelToViewModel", "Lcom/adhoclabs/burner/features/messaging/models/MessagingContactDataModel;", "Lcom/adhoclabs/burner/features/messaging/models/MessagingContactViewModel;", "messagingMessageDataModelToViewModel", "Lcom/adhoclabs/burner/features/messaging/models/MessagingMessageViewModel;", "colorMap", "Lcom/adhoclabs/burner/infra/utils/color/ColorMap;", "messaging_release"}, k = 1, mv = {2, 0, 0}, xi = 48)
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\feature\groups\messaging\di\MessagingGroupMessagingModule.java:99`
```
public final MessagingContract.Interactor provideMessagingInteractor(MessagingAnalyticsReporter analytics, @MessagingGroup MessagingShim messagingShim, ClipboardManager clipboardManager, @IODispatcher CoroutineDispatcher dispatcher, @IOScope CoroutineScope scope, @MainDispatcher CoroutineDispatcher uiDispatcher, MessagingContract.Repository repository, @MessagingGroup MessagingContract.Router router, Mapper<GetMessagesResult, MessagingDataModel> getMessagesResultToMessagingDataModel, MutableStateFlow<ContentState<MessagingDataModel>> initialState, PhoneUtil phoneUtil, Logger log, Cache<List<MessagingMessageDataModel>> failedMessages, BlockingCreator<LocalMessageCreator.Input, MessagingMessageDataModel> localMessageCreator, @AudioMediaPlayer AudioMediaManager audioMediaManager, UseCaseMutator<AudioMediaManager.Media> setPreparedMedia, ContactsRepository contactsRepository) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\feature\groups\messaging\di\MessagingGroupMessagingModule_Companion_ProvideMessagingInteractorFactory.java:5`
```
import com.adhoclabs.burner.features.infra.clipboard.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\feature\groups\messaging\di\MessagingGroupMessagingModule_Companion_ProvideMessagingInteractorFactory.java:32`
```
private final Provider<ClipboardManager> clipboardManagerProvider;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\feature\groups\messaging\di\MessagingGroupMessagingModule_Companion_ProvideMessagingInteractorFactory.java:48`
```
public MessagingGroupMessagingModule_Companion_ProvideMessagingInteractorFactory(Provider<MessagingAnalyticsReporter> analyticsProvider, Provider<MessagingShim> messagingShimProvider, Provider<ClipboardManager> clipboardManagerProvider, Provider<CoroutineDispatcher> dispatcherProvider, Provider<CoroutineScope> scopeProvider, Provider<CoroutineDispatcher> uiDispatcherProvider, Provider<MessagingContract.Repository> repositoryProvider, Provider<MessagingContract.Router> routerProvider, Provider<Mapper<GetMessagesResult, MessagingDataModel>> getMessagesResultToMessagingDataModelProvider, Provider<MutableStateFlow<ContentState<MessagingDataModel>>> initialStateProvider, Provider<PhoneUtil> phoneUtilProvider, Provider<Logger> logProvider, Provider<Cache<List<MessagingMessageDataModel>>> failedMessagesProvider, Provider<BlockingCreator<LocalMessageCreator.Input, MessagingMessageDataModel>> localMessageCreatorProvider, Provider<AudioMediaManager> audioMediaManagerProvider, Provider<UseCaseMutator<AudioMediaManager.Media>> setPreparedMediaProvider, Provider<ContactsRepository> contactsRepositoryProvider) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\feature\groups\messaging\di\MessagingGroupMessagingModule_Companion_ProvideMessagingInteractorFactory.java:73`
```
public static MessagingGroupMessagingModule_Companion_ProvideMessagingInteractorFactory create(Provider<MessagingAnalyticsReporter> analyticsProvider, Provider<MessagingShim> messagingShimProvider, Provider<ClipboardManager> clipboardManagerProvider, Provider<CoroutineDispatcher> dispatcherProvider, Provider<CoroutineScope> scopeProvider, Provider<CoroutineDispatcher> uiDispatcherProvider, Provider<MessagingContract.Repository> repositoryProvider, Provider<MessagingContract.Router> routerProvider, Provider<Mapper<GetMessagesResult, MessagingDataModel>> getMessagesResultToMessagingDataModelProvider, Provider<MutableStateFlow<ContentState<MessagingDataModel>>> initialStateProvider, Provider<PhoneUtil> phoneUtilProvider, Provider<Logger> logProvider, Provider<Cache<List<MessagingMessageDataModel>>> failedMessagesProvider, Provider<BlockingCreator<LocalMessageCreator.Input, MessagingMessageDataModel>> localMessageCreatorProvider, Provider<AudioMediaManager> audioMediaManagerProvider, Provider<UseCaseMutator<AudioMediaManager.Media>> setPreparedMediaProvider, Provider<ContactsRepository> contactsRepositoryProvider) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\feature\groups\messaging\di\MessagingGroupMessagingModule_Companion_ProvideMessagingInteractorFactory.java:77`
```
public static MessagingContract.Interactor provideMessagingInteractor(MessagingAnalyticsReporter analytics, MessagingShim messagingShim, ClipboardManager clipboardManager, CoroutineDispatcher dispatcher, CoroutineScope scope, CoroutineDispatcher uiDispatcher, MessagingContract.Repository repository, MessagingContract.Router router, Mapper<GetMessagesResult, MessagingDataModel> getMessagesResultToMessagingDataModel, MutableStateFlow<ContentState<MessagingDataModel>> initialState, PhoneUtil phoneUtil, Logger log, Cache<List<MessagingMessageDataModel>> failedMessages, BlockingCreator<LocalMessageCreator.Input, MessagingMessageDataModel> localMessageCreator, AudioMediaManager audioMediaManager, UseCaseMutator<AudioMediaManager.Media> setPreparedMedia, ContactsRepository contactsRepository) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\dev\tools\ui\composables\DevToolsScreenKt.java:24`
```
import androidx.compose.ui.platform.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\dev\tools\ui\composables\DevToolsScreenKt.java:350`
```
ProvidableCompositionLocal<ClipboardManager> localClipboardManager = CompositionLocalsKt.getLocalClipboardManager();
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\dev\tools\ui\composables\DevToolsScreenKt.java:352`
```
Object objConsume = composerStartRestartGroup.consume(localClipboardManager);
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\dev\tools\ui\composables\DevToolsScreenKt.java:354`
```
final ClipboardManager clipboardManager = (ClipboardManager) objConsume;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\dev\tools\ui\composables\DevToolsScreenKt.java:402`
```
public static final Unit UserSection$lambda$14$lambda$13(ClipboardManager clipboardManager, String str) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\ClipboardManager.java:5`
```
/* compiled from: ClipboardManager.kt */
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\ClipboardManager.java:6`
```
@Metadata(d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\bf\u0018\u00002\u00020\u0001R\u001a\u0010\u0002\u001a\u0004\u0018\u00010\u0003X¦\u000e¢\u0006\f\u001a\u0004\b\u0004\u0010\u0005\"\u0004\b\u0006\u0010\u0007¨\u0006\b"}, d2 = {"Lcom/adhoclabs/burner/features/infra/clipboard/ClipboardManager;", "", "text", "", "getText", "()Ljava/lang/String;", "setText", "(Ljava/lang/String;)V", "clipboard_release"}, k = 1, mv = {2, 0, 0}, xi = 48)
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\ClipboardManager.java:8`
```
public interface ClipboardManager {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule.java:4`
```
import com.adhoclabs.burner.features.infra.clipboard.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule.java:5`
```
import com.adhoclabs.burner.features.infra.clipboard.impl.ClipboardManagerImpl;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule.java:15`
```
/* compiled from: ClipboardManagerModule.kt */
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule.java:16`
```
@Metadata(d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\b!\u0018\u0000 \b2\u00020\u0001:\u0001\bB\u0007¢\u0006\u0004\b\u0002\u0010\u0003J\u0010\u0010\u0004\u001a\u00020\u00052\u0006\u0010\u0006\u001a\u00020\u0007H'¨\u0006\t"}, d2 = {"Lcom/adhoclabs/burner/features/infra/clipboard/di/ClipboardManagerModule;", "", MethodDescription.CONSTRUCTOR_INTERNAL_NAME, "()V", "bindsClipboardManager", "Lcom/adhoclabs/burner/features/infra/clipboard/ClipboardManager;", "impl", "Lcom/adhoclabs/burner/features/infra/clipboard/impl/ClipboardManagerImpl;", "Companion", "clipboard_release"}, k = 1, mv = {2, 0, 0}, xi = 48)
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule.java:19`
```
public abstract class ClipboardManagerModule {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule.java:25`
```
public abstract ClipboardManager bindsClipboardManager(ClipboardManagerImpl impl);
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule.java:27`
```
/* compiled from: ClipboardManagerModule.kt */
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule.java:28`
```
@Metadata(d1 = {"\u0000\u0018\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u0003J\u0012\u0010\u0004\u001a\u00020\u00052\b\b\u0001\u0010\u0006\u001a\u00020\u0007H\u0007¨\u0006\b"}, d2 = {"Lcom/adhoclabs/burner/features/infra/clipboard/di/ClipboardManagerModule$Companion;", "", MethodDescription.CONSTRUCTOR_INTERNAL_NAME, "()V", "provideAndroidClipboardManager", "Landroid/content/ClipboardManager;", "context", "Landroid/content/Context;", "clipboard_release"}, k = 1, mv = {2, 0, 0}, xi = 48)
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule.java:38`
```
public final android.content.ClipboardManager provideAndroidClipboardManager(@ApplicationContext Context context) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule.java:42`
```
return (android.content.ClipboardManager) systemService;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory.java:3`
```
import android.content.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory.java:10`
```
public final class ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory implements Factory<ClipboardManager> {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory.java:13`
```
public ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory(Provider<Context> contextProvider) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory.java:18`
```
public ClipboardManager get() {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory.java:19`
```
return provideAndroidClipboardManager(this.contextProvider.get());
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory.java:22`
```
public static ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory create(Provider<Context> contextProvider) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory.java:23`
```
return new ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory(contextProvider);
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory.java:26`
```
public static ClipboardManager provideAndroidClipboardManager(Context context) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\ClipboardManagerModule_Companion_ProvideAndroidClipboardManagerFactory.java:27`
```
return (ClipboardManager) Preconditions.checkNotNullFromProvides(ClipboardManagerModule.INSTANCE.provideAndroidClipboardManager(context));
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\HiltWrapper_ClipboardManagerModule.java:5`
```
@Module(includes = {ClipboardManagerModule.class})
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\di\HiltWrapper_ClipboardManagerModule.java:7`
```
public final class HiltWrapper_ClipboardManagerModule {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl.java:4`
```
import com.adhoclabs.burner.features.infra.clipboard.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl.java:10`
```
/* compiled from: ClipboardManagerImpl.kt */
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl.java:11`
```
@Metadata(d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0002\b\u0006\b\u0000\u0018\u00002\u00020\u0001B\u0011\b\u0007\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u0004\b\u0004\u0010\u0005R\u000e\u0010\u0002\u001a\u00020\u0003X\u0082\u0004¢\u0006\u0002\n\u0000R(\u0010\b\u001a\u0004\u0018\u00010\u00072\b\u0010\u0006\u001a\u0004\u0018\u00010\u00078V@VX\u0096\u000e¢\u0006\f\u001a\u0004\b\t\u0010\n\"\u0004\b\u000b\u0010\f¨\u0006\r"}, d2 = {"Lcom/adhoclabs/burner/features/infra/clipboard/impl/ClipboardManagerImpl;", "Lcom/adhoclabs/burner/features/infra/clipboard/ClipboardManager;", "clipboardManager", "Landroid/content/ClipboardManager;", MethodDescription.CONSTRUCTOR_INTERNAL_NAME, "(Landroid/content/ClipboardManager;)V", "value", "", "text", "getText", "()Ljava/lang/String;", "setText", "(Ljava/lang/String;)V", "clipboard_release"}, k = 1, mv = {2, 0, 0}, xi = 48)
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl.java:13`
```
public final class ClipboardManagerImpl implements ClipboardManager {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl.java:14`
```
private final android.content.ClipboardManager clipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl.java:17`
```
public ClipboardManagerImpl(android.content.ClipboardManager clipboardManager) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl.java:22`
```
@Override // com.adhoclabs.burner.features.infra.clipboard.ClipboardManager
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl.java:28`
```
@Override // com.adhoclabs.burner.features.infra.clipboard.ClipboardManager
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl_Factory.java:3`
```
import android.content.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl_Factory.java:8`
```
public final class ClipboardManagerImpl_Factory implements Factory<ClipboardManagerImpl> {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl_Factory.java:9`
```
private final Provider<ClipboardManager> clipboardManagerProvider;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl_Factory.java:11`
```
public ClipboardManagerImpl_Factory(Provider<ClipboardManager> clipboardManagerProvider) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl_Factory.java:16`
```
public ClipboardManagerImpl get() {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl_Factory.java:20`
```
public static ClipboardManagerImpl_Factory create(Provider<ClipboardManager> clipboardManagerProvider) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl_Factory.java:21`
```
return new ClipboardManagerImpl_Factory(clipboardManagerProvider);
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl_Factory.java:24`
```
public static ClipboardManagerImpl newInstance(ClipboardManager clipboardManager) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\clipboard\impl\ClipboardManagerImpl_Factory.java:25`
```
return new ClipboardManagerImpl(clipboardManager);
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\utils\context\ContextExtKt.java:4`
```
import android.content.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\infra\utils\context\ContextExtKt.java:78`
```
ClipboardManager clipboardManager = (ClipboardManager) ContextCompat.getSystemService(context, ClipboardManager.class);
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\messaging\impl\MessagingInteractor.java:10`
```
import com.adhoclabs.burner.features.infra.clipboard.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\messaging\impl\MessagingInteractor.java:69`
```
@Metadata(d1 = {"\u0000ö\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u0003\n\u0002\b\u0004\b\u0007\u0018\u00002\u00020\u0001BÓ\u0001\u0012\b\b\u0001\u0010\u0002\u001a\u00020\u0003\u0012\u0006\u0010\u0004\u001a\u00020\u0005\u0012\u0006\u0010\u0006\u001a\u00020\u0007\u0012\u0006\u0010\b\u001a\u00020\t\u0012\b\b\u0001\u0010\n\u001a\u00020\u000b\u0012\b\b\u0001\u0010\f\u001a\u00020\r\u0012\b\b\u0001\u0010\u000e\u001a\u00020\u000b\u0012\u0006\u0010\u000f\u001a\u00020\u0010\u0012\u0006\u0010\u0011\u001a\u00020\u0012\u0012\u0012\u0010\u0013\u001a\u000e\u0012\u0004\u0012\u00020\u0015\u0012\u0004\u0012\u00020\u00160\u0014\u0012\u0012\u0010\u0017\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020\u00160\u00190\u0018\u0012\u0006\u0010\u001a\u001a\u00020\u001b\u0012\n\u0010\u001c\u001a\u00060\u001dj\u0002`\u001e\u0012\u0012\u0010\u001f\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020\"0!0 \u0012\u0012\u0010#\u001a\u000e\u0012\u0004\u0012\u00020%\u0012\u0004\u0012\u00020\"0$\u0012\u000e\u0010&\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010(0'\u0012\u0006\u0010)\u001a\u00020*¢\u0006\u0004\b+\u0010,J\u0016\u00103\u001a\b\u0012\u0004\u0012\u000205042\u0006\u00106\u001a\u000207H\u0016J\u0010\u00108\u001a\u0002092\u0006\u0010:\u001a\u00020;H\u0016J\u0018\u0010<\u001a\u0002092\u0006\u0010=\u001a\u00020>2\u0006\u0010?\u001a\u00020@H\u0016J\b\u0010A\u001a\u000209H\u0016J\u0010\u0010B\u001a\u0002092\u0006\u0010C\u001a\u00020\"H\u0016J\u0016\u0010D\u001a\u0002092\u0006\u0010E\u001a\u00020FH\u0096@¢\u0006\u0002\u0010GJ\u0016\u0010H\u001a\u0002092\u0006\u0010I\u001a\u00020>H\u0096@¢\u0006\u0002\u0010JJ \u0010K\u001a\u0002092\u0006\u0010L\u001a\u00020M2\u0006\u0010I\u001a\u00020>2\u0006\u0010N\u001a\u00020@H\u0002J\u0018\u0010O\u001a\u0002092\u0006\u0010L\u001a\u00020M2\u0006\u0010I\u001a\u00020>H\u0002J\u0016\u0010P\u001a\u0002092\u0006\u0010I\u001a\u00020>H\u0096@¢\u0006\u0002\u0010JJ \u0010Q\u001a\u0002092\u0006\u0010R\u001a\u00020\"2\b\u0010S\u001a\u0004\u0018\u00010TH\u0096@¢\u0006\u0002\u0010UJ\b\u0010V\u001a\u000209H\u0016J\b\u0010W\u001a\u000209H\u0016J\b\u0010X\u001a\u000209H\u0016J\b\u0010Y\u001a\u000209H\u0016J\u0016\u0010Z\u001a\u0002092\u0006\u0010E\u001a\u00020[H\u0097@¢\u0006\u0002\u0010\\J \u0010]\u001a\u0002092\u0006\u0010^\u001a\u00020\u00162\b\u0010R\u001a\u0004\u0018\u00010\"H\u0082@¢\u0006\u0002\u0010_J\u001e\u0010`\u001a\u0002092\u0006\u0010^\u001a\u00020\u00162\u0006\u0010a\u001a\u00020bH\u0082@¢\u0006\u0002\u0010cJ\u001e\u0010d\u001a\u0002092\u0006\u0010e\u001a\u00020%2\u0006\u0010f\u001a\u00020gH\u0082@¢\u0006\u0002\u0010hJ\u0016\u0010i\u001a\u0002092\u0006\u00106\u001a\u000207H\u0082@¢\u0006\u0002\u0010jR\u000e\u0010\u0002\u001a\u00020\u0003X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\u0004\u001a\u00020\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\u0006\u001a\u00020\u0007X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\b\u001a\u00020\tX\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\n\u001a\u00020\u000bX\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\f\u001a\u00020\rX\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\u000e\u001a\u00020\u000bX\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\u000f\u001a\u00020\u0010X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\u0011\u001a\u00020\u0012X\u0082\u0004¢\u0006\u0002\n\u0000R\u001a\u0010\u0013\u001a\u000e\u0012\u0004\u0012\u00020\u0015\u0012\u0004\u0012\u00020\u00160\u0014X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\u001a\u001a\u00020\u001bX\u0082\u0004¢\u0006\u0002\n\u0000R\u0012\u0010\u001c\u001a\u00060\u001dj\u0002`\u001eX\u0082\u0004¢\u0006\u0002\n\u0000R\u001a\u0010\u001f\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020\"0!0 X\u0082\u0004¢\u0006\u0002\n\u0000R\u001a\u0010#\u001a\u000e\u0012\u0004\u0012\u00020%\u0012\u0004\u0012\u00020\"0$X\u0082\u0004¢\u0006\u0002\n\u0000R\u0016\u0010&\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010(0'X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010)\u001a\u00020*X\u0082\u0004¢\u0006\u0002\n\u0000R\u001a\u0010-\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020\u00160\u00190\u0018X\u0082\u0004¢\u0006\u0002\n\u0000R\u001a\u0010.\u001a\b\u0012\u0004\u0012\u0002000/X\u0096\u0004¢\u0006\b\n\u0000\u001a\u0004\b1\u00102¨\u0006k"}, d2 = {"Lcom/adhoclabs/burner/features/messaging/impl/MessagingInteractor;", "Lcom/adhoclabs/burner/features/messaging/MessagingContract$Interactor;", "audioMediaManager", "Lcom/adhoclabs/burner/features/infra/audio/AudioMediaManager;", "analytics", "Lcom/adhoclabs/burner/infra/analytics/MessagingAnalyticsReporter;", "messagingShim", "Lcom/adhoclabs/burner/features/messaging/MessagingShim;", "clipboardManager", "Lcom/adhoclabs/burner/features/infra/clipboard/ClipboardManager;", "dispatcher", "Lkotlinx/coroutines/CoroutineDispatcher;", "scope", "Lkotlinx/coroutines/CoroutineScope;", "uiDispatcher", "repository", "Lcom/adhoclabs/burner/features/messaging/MessagingContract$Repository;", "router", "Lcom/adhoclabs/burner/features/messaging/MessagingContract$Router;", "getMessagesResultToMessagingDataModel", "Lcom/adhoclabs/burner/infra/mapper/Mapper;", "Lcom/adhoclabs/burner/features/messaging/models/GetMessagesResult;", "Lcom/adhoclabs/burner/features/messaging/impl/MessagingDataModel;", "initialState", "Lkotlinx/coroutines/flow/MutableStateFlow;", "Lcom/adhoclabs/burner/features/infra/state/ContentState;", "phoneUtil", "Lcom/adhoclabs/burner/infra/utils/phone/PhoneUtil;", "log", "Lco/adhoclabs/burner/core/logging/Logger;", "Lcom/adhoclabs/burner/infra/logger/Logger;", "localMessages", "Lcom/adhoclabs/burner/infra/storage/cache/Cache;", "", "Lcom/adhoclabs/burner/features/messaging/models/MessagingMessageDataModel;", "localMessageCreator", "Lcom/adhoclabs/burner/infra/creator/BlockingCreator;", "Lcom/adhoclabs/burner/features/messaging/impl/LocalMessageCreator$Input;", "setPreparedMedia", "Lcom/adhoclabs/burner/infra/usecase/UseCaseMutator;", "Lcom/adhoclabs/burner/features/infra/audio/AudioMediaManager$Media;", "contactsRepository", "Lcom/adhoclabs/burner/infra/repositories/contacts/ContactsRepository;", MethodDescription.CONSTRUCTOR_INTERNAL_NAME, "(Lcom/adhoclabs/burner/features/infra/audio/AudioMediaManager;Lcom/adhoclabs/burner/infra/analytics/MessagingAnalyticsReporter;Lcom/adhoclabs/burner/features/messaging/MessagingShim;Lcom/adhoclabs/burner/features/infra/clipboard/ClipboardManager;Lkotlinx/coroutines/CoroutineDispatcher;Lkotlinx/coroutines/CoroutineScope;Lkotlinx/coroutines/CoroutineDispatcher;Lcom/adhoclabs/burner/features/messaging/MessagingContract$Repository;Lcom/adhoclabs/burner/features/messaging/MessagingContract$Router;Lcom/adhoclabs/burner/infra/mapper/Mapper;Lkotlinx/coroutines/flow/MutableStateFlow;Lcom/adhoclabs/burner/infra/utils/phone/PhoneUtil;Lco/adhoclabs/burner/core/logging/Logger;Lcom/adhoclabs/burner/infra/storage/cache/Cache;Lcom/adhoclabs/burner/infra/creator/BlockingCreator;Lcom/adhoclabs/burner/infra/usecase/UseCaseMutator;Lcom/adhoclabs/burner/infra/repositories/contacts/ContactsRepository;)V", "state", "onError", "Lkotlinx/coroutines/flow/MutableSharedFlow;", "Lcom/adhoclabs/burner/features/messaging/MessagingContract$Error;", "getOnError", "()Lkotlinx/coroutines/flow/MutableSharedFlow;", "getDataModel", "Lkotlinx/coroutines/flow/Flow;", "Lcom/adhoclabs/burner/features/messaging/MessagingContract$DataModel;", "conversationId", "Lcom/adhoclabs/burner/feature/messaging/model/ConversationId;", "onViewMmsAttachmentClicked", "", "mmsAttachment", "Lcom/adhoclabs/burner/features/infra/composer/MmsAttachment$Valid;", "onAiVoicemailRated", "messageId", "", "positiveRating", "", "onAiVoicemailViewAnywayClick", "copy", "message", "delete", NativeProtocol.WEB_DIALOG_ACTION, "Lcom/adhoclabs/burner/features/messaging/MessagingContract$Interactor$DeleteAction;", "(Lcom/adhoclabs/burner/features/messaging/MessagingContract$Interactor$DeleteAction;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "call", "phoneNumber", "(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "showFirstCallDialogOrMakeCall", "burner", "Lcom/adhoclabs/burner/burner/api/model/Burner;", "isFirstTimeCalling", "makeCall", "onMakeFirstCall", "onMessageClick", "dataModel", "messageClickData", "Lcom/adhoclabs/burner/features/messaging/models/MessageClickData;", "(Lcom/adhoclabs/burner/features/messaging/models/MessagingMessageDataModel;Lcom/adhoclabs/burner/features/messaging/models/MessageClickData;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "onAddAttachmentClick", "onGoToContactClick", "onMuteClick", "onBlockClick", "onSendClick", "Lcom/adhoclabs/burner/features/messaging/common/MessageSendAction;", "(Lcom/adhoclabs/burner/features/messaging/common/MessageSendAction;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "sendFailedMessage", DeviceRequestsHelper.DEVICE_INFO_MODEL, "(Lcom/adhoclabs/burner/features/messaging/impl/MessagingDataModel;Lcom/adhoclabs/burner/features/messaging/models/MessagingMessageDataModel;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "sendNewMessage", "sendAction", "Lcom/adhoclabs/burner/features/messaging/common/MessageSendAction$New;", "(Lcom/adhoclabs/burner/features/messaging/impl/MessagingDataModel;Lcom/adhoclabs/burner/features/messaging/common/MessageSendAction$New;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "handleSendNewMessageFailure", "localMessageInput", "throwable", "", "(Lcom/adhoclabs/burner/features/messaging/impl/LocalMessageCreator$Input;Ljava/lang/Throwable;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "readConversation", "(Lcom/adhoclabs/burner/feature/messaging/model/ConversationId;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "messaging_release"}, k = 1, mv = {2, 0, 0}, xi = 48)
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\messaging\impl\MessagingInteractor.java:75`
```
private final ClipboardManager clipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\features\messaging\impl\MessagingInteractor.java:226`
```
public MessagingInteractor(@AudioMediaPlayer AudioMediaManager audioMediaManager, MessagingAnalyticsReporter analytics, MessagingShim messagingShim, ClipboardManager clipboardManager, @IODispatcher CoroutineDispatcher dispatcher, @IOScope CoroutineScope scope, @MainDispatcher CoroutineDispatcher uiDispatcher, MessagingContract.Repository repository, MessagingContract.Router router, Mapper<GetMessagesResult, MessagingDataModel> getMessagesResultToMessagingDataModel, MutableStateFlow<ContentState<MessagingDataModel>> initialState, PhoneUtil phoneUtil, Logger log, Cache<List<MessagingMessageDataModel>> localMessages, BlockingCreator<LocalMessageCreator.Input, MessagingMessageDataModel> localMessageCreator, UseCaseMutator<AudioMediaManager.Media> setPreparedMedia, ContactsRepository contactsRepository) {
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\common\extensions\ContextExtensionsKt.java:4`
```
import android.content.ClipboardManager;
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_CLIPBOARD_PII (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\common\extensions\ContextExtensionsKt.java:110`
```
ClipboardManager clipboardManager = (ClipboardManager) ContextCompat.getSystemService(addToClipboard, ClipboardManager.class);
```
- **Why it matters:** Clipboard usage with potential PII in project; verify no sensitive data copied.

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\db\AppDatabase_Impl.java:14`
```
import androidx.sqlite.db.SupportSQLiteOpenHelper;
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\db\AppDatabase_Impl.java:43`
```
@Metadata(d1 = {"\u0000j\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010$\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0010 \n\u0000\n\u0002\u0010\"\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0007\b\u0007\u0018\u00002\u00020\u0001B\t\b\u0007¢\u0006\u0004\b\u0002\u0010\u0003J\u0010\u0010\u000f\u001a\u00020\u00102\u0006\u0010\u0011\u001a\u00020\u0012H\u0014J\b\u0010\u0013\u001a\u00020\u0014H\u0014J\b\u0010\u0015\u001a\u00020\u0016H\u0016J*\u0010\u0017\u001a$\u0012\f\u0012\n\u0012\u0006\b\u0001\u0012\u00020\u001a0\u0019\u0012\u0012\u0012\u0010\u0012\f\u0012\n\u0012\u0006\b\u0001\u0012\u00020\u001a0\u00190\u001b0\u0018H\u0014J\u0016\u0010\u001c\u001a\u0010\u0012\f\u0012\n\u0012\u0006\b\u0001\u0012\u00020\u001e0\u00190\u001dH\u0016J*\u0010\u001f\u001a\b\u0012\u0004\u0012\u00020 0\u001b2\u001a\u0010!\u001a\u0016\u0012\f\u0012\n\u0012\u0006\b\u0001\u0012\u00020\u001e0\u0019\u0012\u0004\u0012\u00020\u001e0\u0018H\u0016J\b\u0010\"\u001a\u00020\u0006H\u0016J\b\u0010#\u001a\u00020\bH\u0016J\b\u0010$\u001a\u00020\nH\u0016J\b\u0010%\u001a\u00020\fH\u0016J\b\u0010&\u001a\u00020\u000eH\u0016R\u0014\u0010\u0004\u001a\b\u0012\u0004\u0012\u00020\u00060\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u0014\u0010\u0007\u001a\b\u0012\u0004\u0012\u00020\b0\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u0014\u0010\t\u001a\b\u0012\u0004\u0012\u00020\n0\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u0014\u0010\u000b\u001a\b\u0012\u0004\u0012\u00020\f0\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u0014\u0010\r\u001a\b\u0012\u0004\u0012\u00020\u000e0\u0005X\u0082\u0004¢\u0006\u0002\n\u0000¨\u0006'"}, d2 = {"Lcom/adhoclabs/burner/db/AppDatabase_Impl;", "Lcom/adhoclabs/burner/db/AppDatabase;", MethodDescription.CONSTRUCTOR_INTERNAL_NAME, "()V", "_creditPricingDao", "Lkotlin/Lazy;", "Lco/adhoclabs/burner/features/subscription/management/data/local/dao/CreditPricingDao;", "_creditProductDao", "Lco/adhoclabs/burner/features/subscription/management/data/local/dao/CreditProductDao;", "_subscriptionManagementSkuDao", "Lco/adhoclabs/burner/features/subscription/management/data/local/dao/SubscriptionManagementSkuDao;", "_subscriptionPricingDao", "Lco/adhoclabs/burner/features/subscription/management/data/local/dao/SubscriptionPricingDao;", "_subscriptionProductDao", "Lco/adhoclabs/burner/features/subscription/management/data/local/dao/SubscriptionProductDao;", "createOpenHelper", "Landroidx/sqlite/db/SupportSQLiteOpenHelper;", "config", "Landroidx/room/DatabaseConfiguration;", "createInvalidationTracker", "Landroidx/room/InvalidationTracker;", "clearAllTables", "", "getRequiredTypeConverters", "", "Ljava/lang/Class;", "", "", "getRequiredAutoMigrationSpecs", "", "Landroidx/room/migration/AutoMigrationSpec;", "getAutoMigrations", "Landroidx/room/migration/Migration;", "autoMigrationSpecs", "creditPricingDao", "creditProductDao", "subscriptionManagementSkuDao", "subscriptionPricingDao", "subscriptionProductDao", "app_release"}, k = 1, mv = {2, 0, 0}, xi = 48)
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\db\AppDatabase_Impl.java:104`
```
protected SupportSQLiteOpenHelper createOpenHelper(DatabaseConfiguration config) {
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\db\AppDatabase_Impl.java:106`
```
return config.sqliteOpenHelperFactory.create(SupportSQLiteOpenHelper.Configuration.INSTANCE.builder(config.context).name(config.name).callback(new RoomOpenHelper(config, new RoomOpenHelper.Delegate() { // from class: com.adhoclabs.burner.db.AppDatabase_Impl$createOpenHelper$_openCallback$1
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\feature\messaging\domain\di\MessagesHilt.java:140`
```
@Override // androidx.sqlite.db.SupportSQLiteOpenHelper.Callback
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\storage\database\room\BurnerRoomDatabase_Impl.java:14`
```
import androidx.sqlite.db.SupportSQLiteOpenHelper;
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\storage\database\room\BurnerRoomDatabase_Impl.java:39`
```
protected SupportSQLiteOpenHelper createOpenHelper(final DatabaseConfiguration config) {
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adhoclabs\burner\infra\storage\database\room\BurnerRoomDatabase_Impl.java:40`
```
return config.sqliteOpenHelperFactory.create(SupportSQLiteOpenHelper.Configuration.builder(config.context).name(config.name).callback(new RoomOpenHelper(config, new RoomOpenHelper.Delegate(2) { // from class: com.adhoclabs.burner.infra.storage.database.room.BurnerRoomDatabase_Impl.1
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\android\migration\DatabaseStorage.java:7`
```
import android.database.sqlite.SQLiteOpenHelper;
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\android\migration\DatabaseStorage.java:23`
```
@Metadata(d1 = {"\u0000z\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\t\n\u0002\b\u0004\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0011\n\u0002\b\u0005\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\f\u0018\u00002\u00020\u0001B\u001d\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u0012\u0006\u0010\u0004\u001a\u00020\u0005\u0012\u0006\u0010\u0006\u001a\u00020\u0007¢\u0006\u0002\u0010\bJ\b\u0010\u0012\u001a\u00020\u0013H\u0002J\u0010\u0010\u0014\u001a\u00020\u00132\u0006\u0010\u0015\u001a\u00020\u0016H\u0002J\u0015\u0010\u0017\u001a\u0004\u0018\u00010\u00182\u0006\u0010\u0019\u001a\u00020\u0005¢\u0006\u0002\u0010\u001aJ\u0010\u0010\u001b\u001a\u0004\u0018\u00010\u00052\u0006\u0010\u0019\u001a\u00020\u0005J\u001a\u0010\u001c\u001a\u0004\u0018\u00010\u001d2\u0006\u0010\u001e\u001a\u00020\u00052\u0006\u0010\u0019\u001a\u00020\u0005H\u0002J\u0010\u0010\u001f\u001a\u00020\u00132\u0006\u0010\u0015\u001a\u00020 H\u0002J\u0010\u0010!\u001a\u00020\u00132\u0006\u0010\"\u001a\u00020#H\u0016J\"\u0010$\u001a\u00020\u00132\b\u0010\"\u001a\u0004\u0018\u00010#2\u0006\u0010%\u001a\u00020\n2\u0006\u0010&\u001a\u00020\nH\u0016JY\u0010'\u001a\u0004\u0018\u00010(2\u0006\u0010\"\u001a\u00020#2\b\u0010\u001e\u001a\u0004\u0018\u00010\u00052\u0010\u0010)\u001a\f\u0012\u0006\u0012\u0004\u0018\u00010\u0005\u0018\u00010*2\b\u0010+\u001a\u0004\u0018\u00010\u00052\u0010\u0010,\u001a\f\u0012\u0006\u0012\u0004\u0018\u00010\u0005\u0018\u00010*2\b\u0010-\u001a\u0004\u0018\u00010\u0005H\u0002¢\u0006\u0002\u0010.J\f\u0010/\u001a\b\u0012\u0004\u0012\u00020100J\u0016\u00102\u001a\b\u0012\u0004\u0012\u000201002\u0006\u0010\u001e\u001a\u00020\u0005H\u0002J\f\u00103\u001a\b\u0012\u0004\u0012\u00020100J\f\u00104\u001a\b\u0012\u0004\u0012\u00020100J\u000e\u00105\u001a\u00020\u00132\u0006\u00106\u001a\u00020\u0018J\u0018\u00107\u001a\u00020\u00132\u0006\u0010\u001e\u001a\u00020\u00052\u0006\u00106\u001a\u00020\u0018H\u0002J\u000e\u00108\u001a\u00020\u00132\u0006\u00106\u001a\u00020\u0018J\u000e\u00109\u001a\u00020\u00132\u0006\u00106\u001a\u00020\u0018J\u000e\u0010:\u001a\u00020\u00132\u0006\u0010\u0019\u001a\u00020\u0005J\u000e\u0010;\u001a\u00020\u00132\u0006\u0010\u0019\u001a\u00020\u0005J\u0018\u0010<\u001a\u00020\u00132\u0006\u0010\u001e\u001a\u00020\u00052\u0006\u0010\u0019\u001a\u00020\u0005H\u0002R\u001e\u0010\u000b\u001a\u00020\n2\u0006\u0010\t\u001a\u00020\n@BX\u0086\u000e¢\u0006\b\n\u0000\u001a\u0004\b\f\u0010\rR\u000e\u0010\u000e\u001a\u00020\u000fX\u0082\u000e¢\u0006\u0002\n\u0000R\u000e\u0010\u0010\u001a\u00020\u0011X\u0082\u000e¢\u0006\u0002\n\u0000R\u000e\u0010\u0006\u001a\u00020\u0007X\u0082\u0004¢\u0006\u0002\n\u0000¨\u0006="}, d2 = {"Lcom/amplitude/android/migration/DatabaseStorage;", "Landroid/database/sqlite/SQLiteOpenHelper;", "context", "Landroid/content/Context;", "databaseName", "", "logger", "Lcom/amplitude/common/Logger;", "(Landroid/content/Context;Ljava/lang/String;Lcom/amplitude/common/Logger;)V", "<set-?>", "", "currentDbVersion", "getCurrentDbVersion", "()I", ShareInternalUtility.STAGING_PARAM, "Ljava/io/File;", "isValidDatabaseFile", "", "closeDb", "", "convertIfCursorWindowException", "e", "Ljava/lang/RuntimeException;", "getLongValue", "", DatabaseConstants.KEY_FIELD, "(Ljava/lang/String;)Ljava/lang/Long;", "getValue", "getValueFromTable", "", "table", "handleIfCursorRowTooLargeException", "Ljava/lang/IllegalStateException;", "onCreate", UserDataStore.DATE_OF_BIRTH, "Landroid/database/sqlite/SQLiteDatabase;", "onUpgrade", "oldVersion", "newVersion", "queryDb", "Landroid/database/Cursor;", "columns", "", "selection", "selectionArgs", "orderBy", "(Landroid/database/sqlite/SQLiteDatabase;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", "readEventsContent", "", "Lorg/json/JSONObject;", "readEventsFromTable", "readIdentifiesContent", "readInterceptedIdentifiesContent", "removeEvent", "rowId", "removeEventFromTable", "removeIdentify", "removeInterceptedIdentify", "removeLongValue", "removeValue", "removeValueFromTable", "android_release"}, k = 1, mv = {1, 5, 1}, xi = 48)
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\android\migration\DatabaseStorage.java:25`
```
public final class DatabaseStorage extends SQLiteOpenHelper {
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\android\migration\DatabaseStorage.java:49`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\android\migration\DatabaseStorage.java:56`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\api\DatabaseHelper.java:10`
```
import android.database.sqlite.SQLiteOpenHelper;
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\api\DatabaseHelper.java:21`
```
class DatabaseHelper extends SQLiteOpenHelper {
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\api\DatabaseHelper.java:78`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\api\DatabaseHelper.java:100`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\datatransport\runtime\scheduling\persistence\SchemaManager.java:6`
```
import android.database.sqlite.SQLiteOpenHelper;
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\datatransport\runtime\scheduling\persistence\SchemaManager.java:13`
```
final class SchemaManager extends SQLiteOpenHelper {
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\datatransport\runtime\scheduling\persistence\SchemaManager.java:140`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\datatransport\runtime\scheduling\persistence\SchemaManager.java:154`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\datatransport\runtime\scheduling\persistence\SchemaManager.java:164`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\datatransport\runtime\scheduling\persistence\SchemaManager.java:170`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\datatransport\runtime\scheduling\persistence\SchemaManager.java:181`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzar.java:7`
```
import android.database.sqlite.SQLiteOpenHelper;
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzar.java:13`
```
final class zzar extends SQLiteOpenHelper {
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzar.java:16`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzar.java:40`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzar.java:44`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzar.java:54`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzar.java:59`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzfs.java:8`
```
import android.database.sqlite.SQLiteOpenHelper;
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzfs.java:12`
```
final class zzfs extends SQLiteOpenHelper {
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzfs.java:15`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzfs.java:35`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzfs.java:39`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzfs.java:49`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\gms\measurement\internal\zzfs.java:54`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\recaptcha\internal\zzaz.java:7`
```
import android.database.sqlite.SQLiteOpenHelper;
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\recaptcha\internal\zzaz.java:17`
```
public final class zzaz extends SQLiteOpenHelper {
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\recaptcha\internal\zzaz.java:26`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\recaptcha\internal\zzaz.java:31`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\google\android\recaptcha\internal\zzaz.java:37`
```
@Override // android.database.sqlite.SQLiteOpenHelper
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\local\db\ChatDatabase_Impl.java:12`
```
import androidx.sqlite.db.SupportSQLiteOpenHelper;
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\local\db\ChatDatabase_Impl.java:100`
```
protected SupportSQLiteOpenHelper createOpenHelper(DatabaseConfiguration databaseConfiguration) {
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### ANDROID_SQLITE_PLAINTEXT (low)
- **Category:** android
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\helpscout\beacon\internal\data\local\db\ChatDatabase_Impl.java:101`
```
return databaseConfiguration.sqliteOpenHelperFactory.create(SupportSQLiteOpenHelper.Configuration.builder(databaseConfiguration.context).name(databaseConfiguration.name).callback(new RoomOpenHelper(databaseConfiguration, new RoomOpenHelper.Delegate(6) { // from class: com.helpscout.beacon.internal.data.local.db.ChatDatabase_Impl.1
```
- **Why it matters:** SQLiteOpenHelper used; ensure sensitive data is encrypted (e.g., SQLCipher).

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:522`
```
ActivityHandler.this.logger.warn("Event tracked before first activity resumed.\nIf it was triggered in the Application class, it might timestamp or even send an install long before the user opens the app.\nPlease check https://github.com/adjust/android_sdk#can-i-trigger-an-event-at-application-launch for more information.", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:979`
```
this.logger.info("Skipping duplicated order ID '%s'", str);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:1018`
```
this.logger.info("Waiting %s seconds before starting first session", Util.SecondsDisplayFormat.format(dDoubleValue));
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:1257`
```
this.logger.info("Push token: '%s'", str2);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:1386`
```
this.logger.debug("Launching success session tracking listener", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:1392`
```
this.logger.debug("Launching failed session tracking listener", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:1400`
```
this.logger.debug("Launching SessionResponse tasks", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:1548`
```
this.logger.debug("Deep link (" + uri.toString() + ") processing skipped", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:1563`
```
this.logger.error("Failed to read %s file (%s)", SESSION_CALLBACK_PARAMETERS_NAME, e2.getMessage());
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:1572`
```
this.logger.error("Failed to read %s file (%s)", SESSION_PARTNER_PARAMETERS_NAME, e2.getMessage());
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:2110`
```
this.logger.debug("Finished tracking session", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:2234`
```
this.logger.warn("Session Callback parameters are not set", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:2253`
```
this.logger.warn("Session Partner parameters are not set", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:2270`
```
this.logger.warn("Session Callback parameters are not set", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\ActivityHandler.java:2283`
```
this.logger.warn("Session Partner parameters are not set", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\AdjustConfig.java:70`
```
this.logger.error("Missing App Token", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\AdjustConfig.java:76`
```
this.logger.error("Malformed App Token '%s'", str);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\InstallReferrer.java:111`
```
this.logger.error("InstallReferrer proxy violating parameter restrictions", new Object[0]);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\InstallReferrer.java:272`
```
this.logger.debug("installReferrer: %s, clickTime: %d, installBeginTime: %d", stringInstallReferrer, Long.valueOf(referrerClickTimestampSeconds), Long.valueOf(installBeginTimestampSeconds));
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\InstallReferrer.java:277`
```
this.logger.debug("installVersion: %s, clickTimeServer: %d, installBeginServer: %d, googlePlayInstant: %b", stringInstallVersion, Long.valueOf(referrerClickTimestampServerSeconds), Long.valueOf(installBeginTimestampServerSeconds), booleanGooglePlayInstantParam);
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\adjust\sdk\InstallReferrer.java:316`
```
this.logger.debug("Already waiting to retry to read install referrer in %d milliseconds", Long.valueOf(fireIn));
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\airbnb\lottie\network\NetworkFetcher.java:134`
```
Logger.debug("Handling zip response.");
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\core\Amplitude.java:688`
```
this.logger.info("Skip event for opt out config.");
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\amplitude\core\utilities\FileResponseHandler.java:392`
```
logger.debug("Back off to retry sending events later.");
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\pusher\client\example\ExampleApp.java:57`
```
System.out.println(String.format("Subscription to channel [%s] succeeded", str));
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\pusher\client\example\PresenceChannelExampleApp.java:64`
```
System.out.println(String.format("Subscription to channel [%s] succeeded", str));
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\pusher\client\example\PresenceChannelExampleApp.java:74`
```
System.out.println(String.format("Authentication failure due to [%s], exception was [%s]", str, exc));
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\pusher\client\example\PrivateChannelExampleApp.java:61`
```
System.out.println(String.format("Subscription to channel [%s] succeeded", str));
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\pusher\client\example\PrivateChannelExampleApp.java:71`
```
System.out.println(String.format("Authentication failure due to [%s], exception was [%s]", str, exc));
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\pusher\client\example\PrivateEncryptedChannelExampleApp.java:61`
```
System.out.println(String.format("Subscription to channel [%s] succeeded", str));
```
- **Why it matters:** Potential sensitive data in log statement.

### GENERIC_LOG_SENSITIVE (low)
- **Category:** privacy
- **File:Line:** `C:\Phd\Research\burner\java_out\sources\com\pusher\client\example\PrivateEncryptedChannelExampleApp.java:71`
```
System.out.println(String.format("Authentication failure due to [%s], exception was [%s]", str, exc));
```
- **Why it matters:** Potential sensitive data in log statement.
