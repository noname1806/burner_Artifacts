// PairIP licensecheck bypass for com.textmeinc.textme (3.55.0)
// Neutralizes the failure/exit path so the app proceeds past LicenseActivity.
Java.perform(function () {
    function safe(name, fn) { try { fn(); console.log('[+] hooked ' + name); } catch (e) { console.log('[-] ' + name + ' : ' + e); } }

    safe('LicenseClient.handleError', function () {
        var LC = Java.use('com.pairip.licensecheck.LicenseClient');
        LC.handleError.implementation = function (ex) {
            console.log('[BYPASS] swallowed LicenseClient.handleError -> ' + ex);
        };
        try { LC.eventualShutdownEnabled.value = false; } catch (_) {}
    });

    safe('LicenseActivity.exit/onStart', function () {
        var LA = Java.use('com.pairip.licensecheck.LicenseActivity');
        LA.exitApp.implementation = function () { console.log('[BYPASS] blocked LicenseActivity.exitApp'); };
        LA.onStart.implementation = function () { console.log('[BYPASS] LicenseActivity.onStart -> finish()'); try { this.finish(); } catch (_) {} };
    });

    safe('System.exit', function () {
        Java.use('java.lang.System').exit.implementation = function (c) { console.log('[BYPASS] blocked System.exit(' + c + ')'); };
    });
    safe('Runtime.exit', function () {
        var RT = Java.use('java.lang.Runtime');
        RT.exit.implementation = function (c) { console.log('[BYPASS] blocked Runtime.exit(' + c + ')'); };
        RT.halt.implementation = function (c) { console.log('[BYPASS] blocked Runtime.halt(' + c + ')'); };
    });
    safe('Process.killProcess', function () {
        Java.use('android.os.Process').killProcess.implementation = function (p) { console.log('[BYPASS] blocked Process.killProcess(' + p + ')'); };
    });

    console.log('[*] PairIP license-bypass hooks installed');
});
