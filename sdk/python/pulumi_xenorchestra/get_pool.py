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
    'GetPoolResult',
    'AwaitableGetPoolResult',
    'get_pool',
    'get_pool_output',
]

warnings.warn("""xenorchestra.index/getpool.getPool has been deprecated in favor of xenorchestra.index/getxoapool.getXoaPool""", DeprecationWarning)

@pulumi.output_type
class GetPoolResult:
    """
    A collection of values returned by getPool.
    """
    def __init__(__self__, cpus=None, description=None, id=None, master=None, name_label=None):
        if cpus and not isinstance(cpus, dict):
            raise TypeError("Expected argument 'cpus' to be a dict")
        pulumi.set(__self__, "cpus", cpus)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if master and not isinstance(master, str):
            raise TypeError("Expected argument 'master' to be a str")
        pulumi.set(__self__, "master", master)
        if name_label and not isinstance(name_label, str):
            raise TypeError("Expected argument 'name_label' to be a str")
        pulumi.set(__self__, "name_label", name_label)

    @property
    @pulumi.getter
    def cpus(self) -> Mapping[str, str]:
        """
        CPU information about the pool. The 'cores' key will contain the number of cpu cores and the 'sockets' key will contain the number of sockets.
        """
        return pulumi.get(self, "cpus")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the pool.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def master(self) -> str:
        """
        The id of the primary instance in the pool.
        """
        return pulumi.get(self, "master")

    @property
    @pulumi.getter(name="nameLabel")
    def name_label(self) -> str:
        """
        The name_label of the pool to look up.
        """
        return pulumi.get(self, "name_label")


class AwaitableGetPoolResult(GetPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPoolResult(
            cpus=self.cpus,
            description=self.description,
            id=self.id,
            master=self.master,
            name_label=self.name_label)


def get_pool(name_label: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPoolResult:
    """
    Provides information about a pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_xenorchestra as xenorchestra

    pool = xenorchestra.get_xoa_pool(name_label="Your pool")
    local_storage = xenorchestra.get_xoa_storage_repository(name_label="Your storage repository label",
        pool_id=pool.id)
    ```


    :param str name_label: The name_label of the pool to look up.
    """
    pulumi.log.warn("""get_pool is deprecated: xenorchestra.index/getpool.getPool has been deprecated in favor of xenorchestra.index/getxoapool.getXoaPool""")
    __args__ = dict()
    __args__['nameLabel'] = name_label
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('xenorchestra:index/getPool:getPool', __args__, opts=opts, typ=GetPoolResult).value

    return AwaitableGetPoolResult(
        cpus=pulumi.get(__ret__, 'cpus'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        master=pulumi.get(__ret__, 'master'),
        name_label=pulumi.get(__ret__, 'name_label'))
def get_pool_output(name_label: Optional[pulumi.Input[str]] = None,
                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPoolResult]:
    """
    Provides information about a pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_xenorchestra as xenorchestra

    pool = xenorchestra.get_xoa_pool(name_label="Your pool")
    local_storage = xenorchestra.get_xoa_storage_repository(name_label="Your storage repository label",
        pool_id=pool.id)
    ```


    :param str name_label: The name_label of the pool to look up.
    """
    pulumi.log.warn("""get_pool is deprecated: xenorchestra.index/getpool.getPool has been deprecated in favor of xenorchestra.index/getxoapool.getXoaPool""")
    __args__ = dict()
    __args__['nameLabel'] = name_label
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('xenorchestra:index/getPool:getPool', __args__, opts=opts, typ=GetPoolResult)
    return __ret__.apply(lambda __response__: GetPoolResult(
        cpus=pulumi.get(__response__, 'cpus'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        master=pulumi.get(__response__, 'master'),
        name_label=pulumi.get(__response__, 'name_label')))
