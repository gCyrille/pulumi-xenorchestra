// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("xenorchestra");

/**
 * Whether SSL should be verified or not. Can be set via the XOA_INSECURE environment variable.
 */
export declare const insecure: boolean | undefined;
Object.defineProperty(exports, "insecure", {
    get() {
        return __config.getObject<boolean>("insecure");
    },
    enumerable: true,
});

/**
 * Password for xoa api. Can be set via the XOA_PASSWORD environment variable.
 */
export declare const password: string | undefined;
Object.defineProperty(exports, "password", {
    get() {
        return __config.get("password");
    },
    enumerable: true,
});

/**
 * If `retryMode` is set, this specifies the duration for which the backoff method will continue retries. Can be set via
 * the `XOA_RETRY_MAX_TIME` environment variable
 */
export declare const retryMaxTime: string | undefined;
Object.defineProperty(exports, "retryMaxTime", {
    get() {
        return __config.get("retryMaxTime");
    },
    enumerable: true,
});

/**
 * Specifies if retries should be attempted for requests that require eventual . Can be set via the XOA_RETRY_MODE
 * environment variable.
 */
export declare const retryMode: string | undefined;
Object.defineProperty(exports, "retryMode", {
    get() {
        return __config.get("retryMode");
    },
    enumerable: true,
});

/**
 * Password for xoa api. Can be set via the XOA_TOKEN environment variable.
 */
export declare const token: string | undefined;
Object.defineProperty(exports, "token", {
    get() {
        return __config.get("token");
    },
    enumerable: true,
});

/**
 * Hostname of the xoa router. Can be set via the XOA_URL environment variable.
 */
export declare const url: string | undefined;
Object.defineProperty(exports, "url", {
    get() {
        return __config.get("url");
    },
    enumerable: true,
});

/**
 * User account for xoa api. Can be set via the XOA_USER environment variable.
 */
export declare const username: string | undefined;
Object.defineProperty(exports, "username", {
    get() {
        return __config.get("username");
    },
    enumerable: true,
});

