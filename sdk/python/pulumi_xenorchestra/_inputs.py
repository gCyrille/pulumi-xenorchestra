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

__all__ = [
    'ResourceSetLimitArgs',
    'ResourceSetLimitArgsDict',
    'VmCdromArgs',
    'VmCdromArgsDict',
    'VmDiskArgs',
    'VmDiskArgsDict',
    'VmNetworkArgs',
    'VmNetworkArgsDict',
]

MYPY = False

if not MYPY:
    class ResourceSetLimitArgsDict(TypedDict):
        quantity: pulumi.Input[int]
        """
        The numerical limit for the given type.
        """
        type: pulumi.Input[str]
        """
        The type of resource set limit. Must be cpus, memory or disk.
        """
elif False:
    ResourceSetLimitArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ResourceSetLimitArgs:
    def __init__(__self__, *,
                 quantity: pulumi.Input[int],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[int] quantity: The numerical limit for the given type.
        :param pulumi.Input[str] type: The type of resource set limit. Must be cpus, memory or disk.
        """
        pulumi.set(__self__, "quantity", quantity)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def quantity(self) -> pulumi.Input[int]:
        """
        The numerical limit for the given type.
        """
        return pulumi.get(self, "quantity")

    @quantity.setter
    def quantity(self, value: pulumi.Input[int]):
        pulumi.set(self, "quantity", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of resource set limit. Must be cpus, memory or disk.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


if not MYPY:
    class VmCdromArgsDict(TypedDict):
        id: pulumi.Input[str]
        """
        The ID of the ISO (VDI) to attach to the VM. This can be easily provided by using the `vdi` data source.
        """
elif False:
    VmCdromArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class VmCdromArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str]):
        """
        :param pulumi.Input[str] id: The ID of the ISO (VDI) to attach to the VM. This can be easily provided by using the `vdi` data source.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The ID of the ISO (VDI) to attach to the VM. This can be easily provided by using the `vdi` data source.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)


if not MYPY:
    class VmDiskArgsDict(TypedDict):
        name_label: pulumi.Input[str]
        """
        The name for the disk
        """
        size: pulumi.Input[int]
        """
        The size in bytes for the disk.
        """
        sr_id: pulumi.Input[str]
        """
        The storage repository ID to use.
        """
        attached: NotRequired[pulumi.Input[bool]]
        """
        Whether the device should be attached to the VM.
        """
        name_description: NotRequired[pulumi.Input[str]]
        """
        The description for the disk
        """
        position: NotRequired[pulumi.Input[str]]
        """
        Indicates the order of the block device.
        """
        vbd_id: NotRequired[pulumi.Input[str]]
        vdi_id: NotRequired[pulumi.Input[str]]
elif False:
    VmDiskArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class VmDiskArgs:
    def __init__(__self__, *,
                 name_label: pulumi.Input[str],
                 size: pulumi.Input[int],
                 sr_id: pulumi.Input[str],
                 attached: Optional[pulumi.Input[bool]] = None,
                 name_description: Optional[pulumi.Input[str]] = None,
                 position: Optional[pulumi.Input[str]] = None,
                 vbd_id: Optional[pulumi.Input[str]] = None,
                 vdi_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name_label: The name for the disk
        :param pulumi.Input[int] size: The size in bytes for the disk.
        :param pulumi.Input[str] sr_id: The storage repository ID to use.
        :param pulumi.Input[bool] attached: Whether the device should be attached to the VM.
        :param pulumi.Input[str] name_description: The description for the disk
        :param pulumi.Input[str] position: Indicates the order of the block device.
        """
        pulumi.set(__self__, "name_label", name_label)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "sr_id", sr_id)
        if attached is not None:
            pulumi.set(__self__, "attached", attached)
        if name_description is not None:
            pulumi.set(__self__, "name_description", name_description)
        if position is not None:
            pulumi.set(__self__, "position", position)
        if vbd_id is not None:
            pulumi.set(__self__, "vbd_id", vbd_id)
        if vdi_id is not None:
            pulumi.set(__self__, "vdi_id", vdi_id)

    @property
    @pulumi.getter(name="nameLabel")
    def name_label(self) -> pulumi.Input[str]:
        """
        The name for the disk
        """
        return pulumi.get(self, "name_label")

    @name_label.setter
    def name_label(self, value: pulumi.Input[str]):
        pulumi.set(self, "name_label", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        """
        The size in bytes for the disk.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="srId")
    def sr_id(self) -> pulumi.Input[str]:
        """
        The storage repository ID to use.
        """
        return pulumi.get(self, "sr_id")

    @sr_id.setter
    def sr_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "sr_id", value)

    @property
    @pulumi.getter
    def attached(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the device should be attached to the VM.
        """
        return pulumi.get(self, "attached")

    @attached.setter
    def attached(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attached", value)

    @property
    @pulumi.getter(name="nameDescription")
    def name_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for the disk
        """
        return pulumi.get(self, "name_description")

    @name_description.setter
    def name_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_description", value)

    @property
    @pulumi.getter
    def position(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates the order of the block device.
        """
        return pulumi.get(self, "position")

    @position.setter
    def position(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "position", value)

    @property
    @pulumi.getter(name="vbdId")
    def vbd_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vbd_id")

    @vbd_id.setter
    def vbd_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vbd_id", value)

    @property
    @pulumi.getter(name="vdiId")
    def vdi_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vdi_id")

    @vdi_id.setter
    def vdi_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vdi_id", value)


if not MYPY:
    class VmNetworkArgsDict(TypedDict):
        network_id: pulumi.Input[str]
        """
        The ID of the network the VM will be on.
        """
        attached: NotRequired[pulumi.Input[bool]]
        """
        Whether the device should be attached to the VM.
        """
        device: NotRequired[pulumi.Input[str]]
        expected_ip_cidr: NotRequired[pulumi.Input[str]]
        ipv4_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        ipv6_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        mac_address: NotRequired[pulumi.Input[str]]
elif False:
    VmNetworkArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class VmNetworkArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[str],
                 attached: Optional[pulumi.Input[bool]] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 expected_ip_cidr: Optional[pulumi.Input[str]] = None,
                 ipv4_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] network_id: The ID of the network the VM will be on.
        :param pulumi.Input[bool] attached: Whether the device should be attached to the VM.
        """
        pulumi.set(__self__, "network_id", network_id)
        if attached is not None:
            pulumi.set(__self__, "attached", attached)
        if device is not None:
            pulumi.set(__self__, "device", device)
        if expected_ip_cidr is not None:
            pulumi.set(__self__, "expected_ip_cidr", expected_ip_cidr)
        if ipv4_addresses is not None:
            pulumi.set(__self__, "ipv4_addresses", ipv4_addresses)
        if ipv6_addresses is not None:
            pulumi.set(__self__, "ipv6_addresses", ipv6_addresses)
        if mac_address is not None:
            pulumi.set(__self__, "mac_address", mac_address)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[str]:
        """
        The ID of the network the VM will be on.
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter
    def attached(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the device should be attached to the VM.
        """
        return pulumi.get(self, "attached")

    @attached.setter
    def attached(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attached", value)

    @property
    @pulumi.getter
    def device(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "device")

    @device.setter
    def device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device", value)

    @property
    @pulumi.getter(name="expectedIpCidr")
    def expected_ip_cidr(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expected_ip_cidr")

    @expected_ip_cidr.setter
    def expected_ip_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expected_ip_cidr", value)

    @property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "ipv4_addresses")

    @ipv4_addresses.setter
    def ipv4_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ipv4_addresses", value)

    @property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "ipv6_addresses")

    @ipv6_addresses.setter
    def ipv6_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ipv6_addresses", value)

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mac_address")

    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac_address", value)


