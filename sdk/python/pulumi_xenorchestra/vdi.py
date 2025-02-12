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

__all__ = ['VdiArgs', 'Vdi']

@pulumi.input_type
class VdiArgs:
    def __init__(__self__, *,
                 filepath: pulumi.Input[str],
                 name_label: pulumi.Input[str],
                 sr_id: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        The set of arguments for constructing a Vdi resource.
        :param pulumi.Input[str] filepath: The file path to the ISO or vdi image that should be uploaded when the VDI is created.
        :param pulumi.Input[str] name_label: The name label of the VDI
        :param pulumi.Input[str] sr_id: The id of the storage repository the VDI should be created in. Make sure the storage repository supports the file you are uploading! For example, ISOs should only be uploaded to ISO storage repositories.
        :param pulumi.Input[str] type: Only `raw` uploads are supported today, but vhd support may be added in the future.
        """
        pulumi.set(__self__, "filepath", filepath)
        pulumi.set(__self__, "name_label", name_label)
        pulumi.set(__self__, "sr_id", sr_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def filepath(self) -> pulumi.Input[str]:
        """
        The file path to the ISO or vdi image that should be uploaded when the VDI is created.
        """
        return pulumi.get(self, "filepath")

    @filepath.setter
    def filepath(self, value: pulumi.Input[str]):
        pulumi.set(self, "filepath", value)

    @property
    @pulumi.getter(name="nameLabel")
    def name_label(self) -> pulumi.Input[str]:
        """
        The name label of the VDI
        """
        return pulumi.get(self, "name_label")

    @name_label.setter
    def name_label(self, value: pulumi.Input[str]):
        pulumi.set(self, "name_label", value)

    @property
    @pulumi.getter(name="srId")
    def sr_id(self) -> pulumi.Input[str]:
        """
        The id of the storage repository the VDI should be created in. Make sure the storage repository supports the file you are uploading! For example, ISOs should only be uploaded to ISO storage repositories.
        """
        return pulumi.get(self, "sr_id")

    @sr_id.setter
    def sr_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "sr_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Only `raw` uploads are supported today, but vhd support may be added in the future.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _VdiState:
    def __init__(__self__, *,
                 filepath: Optional[pulumi.Input[str]] = None,
                 name_label: Optional[pulumi.Input[str]] = None,
                 sr_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Vdi resources.
        :param pulumi.Input[str] filepath: The file path to the ISO or vdi image that should be uploaded when the VDI is created.
        :param pulumi.Input[str] name_label: The name label of the VDI
        :param pulumi.Input[str] sr_id: The id of the storage repository the VDI should be created in. Make sure the storage repository supports the file you are uploading! For example, ISOs should only be uploaded to ISO storage repositories.
        :param pulumi.Input[str] type: Only `raw` uploads are supported today, but vhd support may be added in the future.
        """
        if filepath is not None:
            pulumi.set(__self__, "filepath", filepath)
        if name_label is not None:
            pulumi.set(__self__, "name_label", name_label)
        if sr_id is not None:
            pulumi.set(__self__, "sr_id", sr_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def filepath(self) -> Optional[pulumi.Input[str]]:
        """
        The file path to the ISO or vdi image that should be uploaded when the VDI is created.
        """
        return pulumi.get(self, "filepath")

    @filepath.setter
    def filepath(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filepath", value)

    @property
    @pulumi.getter(name="nameLabel")
    def name_label(self) -> Optional[pulumi.Input[str]]:
        """
        The name label of the VDI
        """
        return pulumi.get(self, "name_label")

    @name_label.setter
    def name_label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_label", value)

    @property
    @pulumi.getter(name="srId")
    def sr_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the storage repository the VDI should be created in. Make sure the storage repository supports the file you are uploading! For example, ISOs should only be uploaded to ISO storage repositories.
        """
        return pulumi.get(self, "sr_id")

    @sr_id.setter
    def sr_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sr_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Only `raw` uploads are supported today, but vhd support may be added in the future.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Vdi(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 filepath: Optional[pulumi.Input[str]] = None,
                 name_label: Optional[pulumi.Input[str]] = None,
                 sr_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a Xen Orchestra vdi resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] filepath: The file path to the ISO or vdi image that should be uploaded when the VDI is created.
        :param pulumi.Input[str] name_label: The name label of the VDI
        :param pulumi.Input[str] sr_id: The id of the storage repository the VDI should be created in. Make sure the storage repository supports the file you are uploading! For example, ISOs should only be uploaded to ISO storage repositories.
        :param pulumi.Input[str] type: Only `raw` uploads are supported today, but vhd support may be added in the future.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VdiArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a Xen Orchestra vdi resource.

        :param str resource_name: The name of the resource.
        :param VdiArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VdiArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 filepath: Optional[pulumi.Input[str]] = None,
                 name_label: Optional[pulumi.Input[str]] = None,
                 sr_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VdiArgs.__new__(VdiArgs)

            if filepath is None and not opts.urn:
                raise TypeError("Missing required property 'filepath'")
            __props__.__dict__["filepath"] = filepath
            if name_label is None and not opts.urn:
                raise TypeError("Missing required property 'name_label'")
            __props__.__dict__["name_label"] = name_label
            if sr_id is None and not opts.urn:
                raise TypeError("Missing required property 'sr_id'")
            __props__.__dict__["sr_id"] = sr_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(Vdi, __self__).__init__(
            'xenorchestra:index/vdi:Vdi',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            filepath: Optional[pulumi.Input[str]] = None,
            name_label: Optional[pulumi.Input[str]] = None,
            sr_id: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Vdi':
        """
        Get an existing Vdi resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] filepath: The file path to the ISO or vdi image that should be uploaded when the VDI is created.
        :param pulumi.Input[str] name_label: The name label of the VDI
        :param pulumi.Input[str] sr_id: The id of the storage repository the VDI should be created in. Make sure the storage repository supports the file you are uploading! For example, ISOs should only be uploaded to ISO storage repositories.
        :param pulumi.Input[str] type: Only `raw` uploads are supported today, but vhd support may be added in the future.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VdiState.__new__(_VdiState)

        __props__.__dict__["filepath"] = filepath
        __props__.__dict__["name_label"] = name_label
        __props__.__dict__["sr_id"] = sr_id
        __props__.__dict__["type"] = type
        return Vdi(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def filepath(self) -> pulumi.Output[str]:
        """
        The file path to the ISO or vdi image that should be uploaded when the VDI is created.
        """
        return pulumi.get(self, "filepath")

    @property
    @pulumi.getter(name="nameLabel")
    def name_label(self) -> pulumi.Output[str]:
        """
        The name label of the VDI
        """
        return pulumi.get(self, "name_label")

    @property
    @pulumi.getter(name="srId")
    def sr_id(self) -> pulumi.Output[str]:
        """
        The id of the storage repository the VDI should be created in. Make sure the storage repository supports the file you are uploading! For example, ISOs should only be uploaded to ISO storage repositories.
        """
        return pulumi.get(self, "sr_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Only `raw` uploads are supported today, but vhd support may be added in the future.
        """
        return pulumi.get(self, "type")

