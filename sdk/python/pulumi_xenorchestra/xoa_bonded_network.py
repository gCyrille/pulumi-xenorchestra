# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = ['XoaBondedNetworkArgs', 'XoaBondedNetwork']

@pulumi.input_type
class XoaBondedNetworkArgs:
    def __init__(__self__, *,
                 name_label: pulumi.Input[str],
                 pool_id: pulumi.Input[str],
                 automatic: Optional[pulumi.Input[bool]] = None,
                 bond_mode: Optional[pulumi.Input[str]] = None,
                 default_is_locked: Optional[pulumi.Input[bool]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name_description: Optional[pulumi.Input[str]] = None,
                 pif_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a XoaBondedNetwork resource.
        :param pulumi.Input[str] name_label: The name label of the network.
        :param pulumi.Input[str] pool_id: The pool id that this network should belong to.
        :param pulumi.Input[str] bond_mode: The bond mode that should be used for this network.
        :param pulumi.Input[bool] default_is_locked: This argument controls whether the network should enforce VIF locking. This defaults to `false` which means that no filtering rules are applied.
        :param pulumi.Input[int] mtu: The MTU of the network. Defaults to `1500` if unspecified.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] pif_ids: The pifs (uuid) that should be used for this network.
        """
        pulumi.set(__self__, "name_label", name_label)
        pulumi.set(__self__, "pool_id", pool_id)
        if automatic is not None:
            pulumi.set(__self__, "automatic", automatic)
        if bond_mode is not None:
            pulumi.set(__self__, "bond_mode", bond_mode)
        if default_is_locked is not None:
            pulumi.set(__self__, "default_is_locked", default_is_locked)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if name_description is not None:
            pulumi.set(__self__, "name_description", name_description)
        if pif_ids is not None:
            pulumi.set(__self__, "pif_ids", pif_ids)

    @property
    @pulumi.getter(name="nameLabel")
    def name_label(self) -> pulumi.Input[str]:
        """
        The name label of the network.
        """
        return pulumi.get(self, "name_label")

    @name_label.setter
    def name_label(self, value: pulumi.Input[str]):
        pulumi.set(self, "name_label", value)

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> pulumi.Input[str]:
        """
        The pool id that this network should belong to.
        """
        return pulumi.get(self, "pool_id")

    @pool_id.setter
    def pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool_id", value)

    @property
    @pulumi.getter
    def automatic(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "automatic")

    @automatic.setter
    def automatic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "automatic", value)

    @property
    @pulumi.getter(name="bondMode")
    def bond_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The bond mode that should be used for this network.
        """
        return pulumi.get(self, "bond_mode")

    @bond_mode.setter
    def bond_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bond_mode", value)

    @property
    @pulumi.getter(name="defaultIsLocked")
    def default_is_locked(self) -> Optional[pulumi.Input[bool]]:
        """
        This argument controls whether the network should enforce VIF locking. This defaults to `false` which means that no filtering rules are applied.
        """
        return pulumi.get(self, "default_is_locked")

    @default_is_locked.setter
    def default_is_locked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "default_is_locked", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        """
        The MTU of the network. Defaults to `1500` if unspecified.
        """
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter(name="nameDescription")
    def name_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name_description")

    @name_description.setter
    def name_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_description", value)

    @property
    @pulumi.getter(name="pifIds")
    def pif_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The pifs (uuid) that should be used for this network.
        """
        return pulumi.get(self, "pif_ids")

    @pif_ids.setter
    def pif_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "pif_ids", value)


@pulumi.input_type
class _XoaBondedNetworkState:
    def __init__(__self__, *,
                 automatic: Optional[pulumi.Input[bool]] = None,
                 bond_mode: Optional[pulumi.Input[str]] = None,
                 default_is_locked: Optional[pulumi.Input[bool]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name_description: Optional[pulumi.Input[str]] = None,
                 name_label: Optional[pulumi.Input[str]] = None,
                 pif_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pool_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering XoaBondedNetwork resources.
        :param pulumi.Input[str] bond_mode: The bond mode that should be used for this network.
        :param pulumi.Input[bool] default_is_locked: This argument controls whether the network should enforce VIF locking. This defaults to `false` which means that no filtering rules are applied.
        :param pulumi.Input[int] mtu: The MTU of the network. Defaults to `1500` if unspecified.
        :param pulumi.Input[str] name_label: The name label of the network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] pif_ids: The pifs (uuid) that should be used for this network.
        :param pulumi.Input[str] pool_id: The pool id that this network should belong to.
        """
        if automatic is not None:
            pulumi.set(__self__, "automatic", automatic)
        if bond_mode is not None:
            pulumi.set(__self__, "bond_mode", bond_mode)
        if default_is_locked is not None:
            pulumi.set(__self__, "default_is_locked", default_is_locked)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if name_description is not None:
            pulumi.set(__self__, "name_description", name_description)
        if name_label is not None:
            pulumi.set(__self__, "name_label", name_label)
        if pif_ids is not None:
            pulumi.set(__self__, "pif_ids", pif_ids)
        if pool_id is not None:
            pulumi.set(__self__, "pool_id", pool_id)

    @property
    @pulumi.getter
    def automatic(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "automatic")

    @automatic.setter
    def automatic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "automatic", value)

    @property
    @pulumi.getter(name="bondMode")
    def bond_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The bond mode that should be used for this network.
        """
        return pulumi.get(self, "bond_mode")

    @bond_mode.setter
    def bond_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bond_mode", value)

    @property
    @pulumi.getter(name="defaultIsLocked")
    def default_is_locked(self) -> Optional[pulumi.Input[bool]]:
        """
        This argument controls whether the network should enforce VIF locking. This defaults to `false` which means that no filtering rules are applied.
        """
        return pulumi.get(self, "default_is_locked")

    @default_is_locked.setter
    def default_is_locked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "default_is_locked", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        """
        The MTU of the network. Defaults to `1500` if unspecified.
        """
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter(name="nameDescription")
    def name_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name_description")

    @name_description.setter
    def name_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_description", value)

    @property
    @pulumi.getter(name="nameLabel")
    def name_label(self) -> Optional[pulumi.Input[str]]:
        """
        The name label of the network.
        """
        return pulumi.get(self, "name_label")

    @name_label.setter
    def name_label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_label", value)

    @property
    @pulumi.getter(name="pifIds")
    def pif_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The pifs (uuid) that should be used for this network.
        """
        return pulumi.get(self, "pif_ids")

    @pif_ids.setter
    def pif_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "pif_ids", value)

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The pool id that this network should belong to.
        """
        return pulumi.get(self, "pool_id")

    @pool_id.setter
    def pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool_id", value)


class XoaBondedNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automatic: Optional[pulumi.Input[bool]] = None,
                 bond_mode: Optional[pulumi.Input[str]] = None,
                 default_is_locked: Optional[pulumi.Input[bool]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name_description: Optional[pulumi.Input[str]] = None,
                 name_label: Optional[pulumi.Input[str]] = None,
                 pif_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A resource for managing Bonded Xen Orchestra networks. See the XCP-ng [networking docs](https://xcp-ng.org/docs/networking.html) for more details.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_xenorchestra as xenorchestra

        host1 = xenorchestra.get_xoa_host(name_label="Your host")
        eth1 = xenorchestra.get_xoa_pif(device="eth1",
            vlan=-1,
            host_id=host1.id)
        eth2 = xenorchestra.get_xoa_pif(device="eth2",
            vlan=-1,
            host_id=host1.id)
        # Create a bonded network from normal PIFs
        network = xenorchestra.XoaBondedNetwork("network",
            name_label="new network name",
            bond_mode="active-backup",
            pool_id=host1.pool_id,
            pif_ids=[
                eth1.id,
                eth2.id,
            ])
        # Create a bonded network from PIFs on VLANs
        eth1_vlan = xenorchestra.get_xoa_pif(device="eth1",
            vlan=15,
            host_id=host1.id)
        eth2_vlan = xenorchestra.get_xoa_pif(device="eth2",
            vlan=15,
            host_id=host1.id)
        # Create a bonded network from normal PIFs
        network_vlan = xenorchestra.XoaBondedNetwork("network_vlan",
            name_label="new network name",
            bond_mode="active-backup",
            pool_id=host1.pool_id,
            pif_ids=[
                eth1_vlan.id,
                eth2_vlan.id,
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bond_mode: The bond mode that should be used for this network.
        :param pulumi.Input[bool] default_is_locked: This argument controls whether the network should enforce VIF locking. This defaults to `false` which means that no filtering rules are applied.
        :param pulumi.Input[int] mtu: The MTU of the network. Defaults to `1500` if unspecified.
        :param pulumi.Input[str] name_label: The name label of the network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] pif_ids: The pifs (uuid) that should be used for this network.
        :param pulumi.Input[str] pool_id: The pool id that this network should belong to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: XoaBondedNetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A resource for managing Bonded Xen Orchestra networks. See the XCP-ng [networking docs](https://xcp-ng.org/docs/networking.html) for more details.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_xenorchestra as xenorchestra

        host1 = xenorchestra.get_xoa_host(name_label="Your host")
        eth1 = xenorchestra.get_xoa_pif(device="eth1",
            vlan=-1,
            host_id=host1.id)
        eth2 = xenorchestra.get_xoa_pif(device="eth2",
            vlan=-1,
            host_id=host1.id)
        # Create a bonded network from normal PIFs
        network = xenorchestra.XoaBondedNetwork("network",
            name_label="new network name",
            bond_mode="active-backup",
            pool_id=host1.pool_id,
            pif_ids=[
                eth1.id,
                eth2.id,
            ])
        # Create a bonded network from PIFs on VLANs
        eth1_vlan = xenorchestra.get_xoa_pif(device="eth1",
            vlan=15,
            host_id=host1.id)
        eth2_vlan = xenorchestra.get_xoa_pif(device="eth2",
            vlan=15,
            host_id=host1.id)
        # Create a bonded network from normal PIFs
        network_vlan = xenorchestra.XoaBondedNetwork("network_vlan",
            name_label="new network name",
            bond_mode="active-backup",
            pool_id=host1.pool_id,
            pif_ids=[
                eth1_vlan.id,
                eth2_vlan.id,
            ])
        ```

        :param str resource_name: The name of the resource.
        :param XoaBondedNetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(XoaBondedNetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automatic: Optional[pulumi.Input[bool]] = None,
                 bond_mode: Optional[pulumi.Input[str]] = None,
                 default_is_locked: Optional[pulumi.Input[bool]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name_description: Optional[pulumi.Input[str]] = None,
                 name_label: Optional[pulumi.Input[str]] = None,
                 pif_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = XoaBondedNetworkArgs.__new__(XoaBondedNetworkArgs)

            __props__.__dict__["automatic"] = automatic
            __props__.__dict__["bond_mode"] = bond_mode
            __props__.__dict__["default_is_locked"] = default_is_locked
            __props__.__dict__["mtu"] = mtu
            __props__.__dict__["name_description"] = name_description
            if name_label is None and not opts.urn:
                raise TypeError("Missing required property 'name_label'")
            __props__.__dict__["name_label"] = name_label
            __props__.__dict__["pif_ids"] = pif_ids
            if pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'pool_id'")
            __props__.__dict__["pool_id"] = pool_id
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="xenorchestra:index/bondedNetwork:BondedNetwork")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(XoaBondedNetwork, __self__).__init__(
            'xenorchestra:index/xoaBondedNetwork:XoaBondedNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            automatic: Optional[pulumi.Input[bool]] = None,
            bond_mode: Optional[pulumi.Input[str]] = None,
            default_is_locked: Optional[pulumi.Input[bool]] = None,
            mtu: Optional[pulumi.Input[int]] = None,
            name_description: Optional[pulumi.Input[str]] = None,
            name_label: Optional[pulumi.Input[str]] = None,
            pif_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            pool_id: Optional[pulumi.Input[str]] = None) -> 'XoaBondedNetwork':
        """
        Get an existing XoaBondedNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bond_mode: The bond mode that should be used for this network.
        :param pulumi.Input[bool] default_is_locked: This argument controls whether the network should enforce VIF locking. This defaults to `false` which means that no filtering rules are applied.
        :param pulumi.Input[int] mtu: The MTU of the network. Defaults to `1500` if unspecified.
        :param pulumi.Input[str] name_label: The name label of the network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] pif_ids: The pifs (uuid) that should be used for this network.
        :param pulumi.Input[str] pool_id: The pool id that this network should belong to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _XoaBondedNetworkState.__new__(_XoaBondedNetworkState)

        __props__.__dict__["automatic"] = automatic
        __props__.__dict__["bond_mode"] = bond_mode
        __props__.__dict__["default_is_locked"] = default_is_locked
        __props__.__dict__["mtu"] = mtu
        __props__.__dict__["name_description"] = name_description
        __props__.__dict__["name_label"] = name_label
        __props__.__dict__["pif_ids"] = pif_ids
        __props__.__dict__["pool_id"] = pool_id
        return XoaBondedNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def automatic(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "automatic")

    @property
    @pulumi.getter(name="bondMode")
    def bond_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The bond mode that should be used for this network.
        """
        return pulumi.get(self, "bond_mode")

    @property
    @pulumi.getter(name="defaultIsLocked")
    def default_is_locked(self) -> pulumi.Output[Optional[bool]]:
        """
        This argument controls whether the network should enforce VIF locking. This defaults to `false` which means that no filtering rules are applied.
        """
        return pulumi.get(self, "default_is_locked")

    @property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[Optional[int]]:
        """
        The MTU of the network. Defaults to `1500` if unspecified.
        """
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter(name="nameDescription")
    def name_description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name_description")

    @property
    @pulumi.getter(name="nameLabel")
    def name_label(self) -> pulumi.Output[str]:
        """
        The name label of the network.
        """
        return pulumi.get(self, "name_label")

    @property
    @pulumi.getter(name="pifIds")
    def pif_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The pifs (uuid) that should be used for this network.
        """
        return pulumi.get(self, "pif_ids")

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> pulumi.Output[str]:
        """
        The pool id that this network should belong to.
        """
        return pulumi.get(self, "pool_id")

