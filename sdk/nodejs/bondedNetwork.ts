// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * A resource for managing Bonded Xen Orchestra networks. See the XCP-ng [networking docs](https://xcp-ng.org/docs/networking.html) for more details.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as xenorchestra from "@pulumi/xenorchestra";
 * import * as xenorchestra from "@vates/pulumi-xenorchestra";
 *
 * const host1 = xenorchestra.getXoaHost({
 *     nameLabel: "Your host",
 * });
 * const eth1 = host1.then(host1 => xenorchestra.getXoaPif({
 *     device: "eth1",
 *     vlan: -1,
 *     hostId: host1.id,
 * }));
 * const eth2 = host1.then(host1 => xenorchestra.getXoaPif({
 *     device: "eth2",
 *     vlan: -1,
 *     hostId: host1.id,
 * }));
 * // Create a bonded network from normal PIFs
 * const network = new xenorchestra.XoaBondedNetwork("network", {
 *     nameLabel: "new network name",
 *     bondMode: "active-backup",
 *     poolId: host1.then(host1 => host1.poolId),
 *     pifIds: [
 *         eth1.then(eth1 => eth1.id),
 *         eth2.then(eth2 => eth2.id),
 *     ],
 * });
 * // Create a bonded network from PIFs on VLANs
 * const eth1Vlan = host1.then(host1 => xenorchestra.getXoaPif({
 *     device: "eth1",
 *     vlan: 15,
 *     hostId: host1.id,
 * }));
 * const eth2Vlan = host1.then(host1 => xenorchestra.getXoaPif({
 *     device: "eth2",
 *     vlan: 15,
 *     hostId: host1.id,
 * }));
 * // Create a bonded network from normal PIFs
 * const networkVlan = new xenorchestra.XoaBondedNetwork("network_vlan", {
 *     nameLabel: "new network name",
 *     bondMode: "active-backup",
 *     poolId: host1.then(host1 => host1.poolId),
 *     pifIds: [
 *         eth1Vlan.then(eth1Vlan => eth1Vlan.id),
 *         eth2Vlan.then(eth2Vlan => eth2Vlan.id),
 *     ],
 * });
 * ```
 *
 * @deprecated xenorchestra.index/bondednetwork.BondedNetwork has been deprecated in favor of xenorchestra.index/xoabondednetwork.XoaBondedNetwork
 */
export class BondedNetwork extends pulumi.CustomResource {
    /**
     * Get an existing BondedNetwork resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BondedNetworkState, opts?: pulumi.CustomResourceOptions): BondedNetwork {
        pulumi.log.warn("BondedNetwork is deprecated: xenorchestra.index/bondednetwork.BondedNetwork has been deprecated in favor of xenorchestra.index/xoabondednetwork.XoaBondedNetwork")
        return new BondedNetwork(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'xenorchestra:index/bondedNetwork:BondedNetwork';

    /**
     * Returns true if the given object is an instance of BondedNetwork.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BondedNetwork {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BondedNetwork.__pulumiType;
    }

    public readonly automatic!: pulumi.Output<boolean | undefined>;
    /**
     * The bond mode that should be used for this network.
     */
    public readonly bondMode!: pulumi.Output<string | undefined>;
    /**
     * This argument controls whether the network should enforce VIF locking. This defaults to `false` which means that no filtering rules are applied.
     */
    public readonly defaultIsLocked!: pulumi.Output<boolean | undefined>;
    /**
     * The MTU of the network. Defaults to `1500` if unspecified.
     */
    public readonly mtu!: pulumi.Output<number | undefined>;
    public readonly nameDescription!: pulumi.Output<string | undefined>;
    /**
     * The name label of the network.
     */
    public readonly nameLabel!: pulumi.Output<string>;
    /**
     * The pifs (uuid) that should be used for this network.
     */
    public readonly pifIds!: pulumi.Output<string[] | undefined>;
    /**
     * The pool id that this network should belong to.
     */
    public readonly poolId!: pulumi.Output<string>;

    /**
     * Create a BondedNetwork resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated xenorchestra.index/bondednetwork.BondedNetwork has been deprecated in favor of xenorchestra.index/xoabondednetwork.XoaBondedNetwork */
    constructor(name: string, args: BondedNetworkArgs, opts?: pulumi.CustomResourceOptions)
    /** @deprecated xenorchestra.index/bondednetwork.BondedNetwork has been deprecated in favor of xenorchestra.index/xoabondednetwork.XoaBondedNetwork */
    constructor(name: string, argsOrState?: BondedNetworkArgs | BondedNetworkState, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("BondedNetwork is deprecated: xenorchestra.index/bondednetwork.BondedNetwork has been deprecated in favor of xenorchestra.index/xoabondednetwork.XoaBondedNetwork")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as BondedNetworkState | undefined;
            resourceInputs["automatic"] = state ? state.automatic : undefined;
            resourceInputs["bondMode"] = state ? state.bondMode : undefined;
            resourceInputs["defaultIsLocked"] = state ? state.defaultIsLocked : undefined;
            resourceInputs["mtu"] = state ? state.mtu : undefined;
            resourceInputs["nameDescription"] = state ? state.nameDescription : undefined;
            resourceInputs["nameLabel"] = state ? state.nameLabel : undefined;
            resourceInputs["pifIds"] = state ? state.pifIds : undefined;
            resourceInputs["poolId"] = state ? state.poolId : undefined;
        } else {
            const args = argsOrState as BondedNetworkArgs | undefined;
            if ((!args || args.nameLabel === undefined) && !opts.urn) {
                throw new Error("Missing required property 'nameLabel'");
            }
            if ((!args || args.poolId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'poolId'");
            }
            resourceInputs["automatic"] = args ? args.automatic : undefined;
            resourceInputs["bondMode"] = args ? args.bondMode : undefined;
            resourceInputs["defaultIsLocked"] = args ? args.defaultIsLocked : undefined;
            resourceInputs["mtu"] = args ? args.mtu : undefined;
            resourceInputs["nameDescription"] = args ? args.nameDescription : undefined;
            resourceInputs["nameLabel"] = args ? args.nameLabel : undefined;
            resourceInputs["pifIds"] = args ? args.pifIds : undefined;
            resourceInputs["poolId"] = args ? args.poolId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(BondedNetwork.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BondedNetwork resources.
 */
export interface BondedNetworkState {
    automatic?: pulumi.Input<boolean>;
    /**
     * The bond mode that should be used for this network.
     */
    bondMode?: pulumi.Input<string>;
    /**
     * This argument controls whether the network should enforce VIF locking. This defaults to `false` which means that no filtering rules are applied.
     */
    defaultIsLocked?: pulumi.Input<boolean>;
    /**
     * The MTU of the network. Defaults to `1500` if unspecified.
     */
    mtu?: pulumi.Input<number>;
    nameDescription?: pulumi.Input<string>;
    /**
     * The name label of the network.
     */
    nameLabel?: pulumi.Input<string>;
    /**
     * The pifs (uuid) that should be used for this network.
     */
    pifIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The pool id that this network should belong to.
     */
    poolId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a BondedNetwork resource.
 */
export interface BondedNetworkArgs {
    automatic?: pulumi.Input<boolean>;
    /**
     * The bond mode that should be used for this network.
     */
    bondMode?: pulumi.Input<string>;
    /**
     * This argument controls whether the network should enforce VIF locking. This defaults to `false` which means that no filtering rules are applied.
     */
    defaultIsLocked?: pulumi.Input<boolean>;
    /**
     * The MTU of the network. Defaults to `1500` if unspecified.
     */
    mtu?: pulumi.Input<number>;
    nameDescription?: pulumi.Input<string>;
    /**
     * The name label of the network.
     */
    nameLabel: pulumi.Input<string>;
    /**
     * The pifs (uuid) that should be used for this network.
     */
    pifIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The pool id that this network should belong to.
     */
    poolId: pulumi.Input<string>;
}
