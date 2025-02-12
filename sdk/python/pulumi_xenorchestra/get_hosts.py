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
from . import outputs

__all__ = [
    'GetHostsResult',
    'AwaitableGetHostsResult',
    'get_hosts',
    'get_hosts_output',
]

warnings.warn("""xenorchestra.index/gethosts.getHosts has been deprecated in favor of xenorchestra.index/getxoahosts.getXoaHosts""", DeprecationWarning)

@pulumi.output_type
class GetHostsResult:
    """
    A collection of values returned by getHosts.
    """
    def __init__(__self__, hosts=None, id=None, master=None, pool_id=None, sort_by=None, sort_order=None, tags=None):
        if hosts and not isinstance(hosts, list):
            raise TypeError("Expected argument 'hosts' to be a list")
        pulumi.set(__self__, "hosts", hosts)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if master and not isinstance(master, str):
            raise TypeError("Expected argument 'master' to be a str")
        pulumi.set(__self__, "master", master)
        if pool_id and not isinstance(pool_id, str):
            raise TypeError("Expected argument 'pool_id' to be a str")
        pulumi.set(__self__, "pool_id", pool_id)
        if sort_by and not isinstance(sort_by, str):
            raise TypeError("Expected argument 'sort_by' to be a str")
        pulumi.set(__self__, "sort_by", sort_by)
        if sort_order and not isinstance(sort_order, str):
            raise TypeError("Expected argument 'sort_order' to be a str")
        pulumi.set(__self__, "sort_order", sort_order)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def hosts(self) -> Sequence['outputs.GetHostsHostResult']:
        """
        The resulting hosts after applying the argument filtering.
        """
        return pulumi.get(self, "hosts")

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
        The primary host of the pool.
        """
        return pulumi.get(self, "master")

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> str:
        """
        The pool id used to filter the resulting hosts by.
        """
        return pulumi.get(self, "pool_id")

    @property
    @pulumi.getter(name="sortBy")
    def sort_by(self) -> Optional[str]:
        """
        The host field to sort the results by (id and name_label are supported).
        """
        return pulumi.get(self, "sort_by")

    @property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[str]:
        """
        Valid options are `asc` or `desc` and sort order is applied to `sort_by` argument.
        """
        return pulumi.get(self, "sort_order")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[str]]:
        """
        The tags (labels) applied to the given entity.
        """
        return pulumi.get(self, "tags")


class AwaitableGetHostsResult(GetHostsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHostsResult(
            hosts=self.hosts,
            id=self.id,
            master=self.master,
            pool_id=self.pool_id,
            sort_by=self.sort_by,
            sort_order=self.sort_order,
            tags=self.tags)


def get_hosts(pool_id: Optional[str] = None,
              sort_by: Optional[str] = None,
              sort_order: Optional[str] = None,
              tags: Optional[Sequence[str]] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHostsResult:
    """
    Use this data source to filter Xenorchestra hosts by certain criteria (name_label, tags) for use in other resources.


    :param str pool_id: The pool id used to filter the resulting hosts by.
    :param str sort_by: The host field to sort the results by (id and name_label are supported).
    :param str sort_order: Valid options are `asc` or `desc` and sort order is applied to `sort_by` argument.
    :param Sequence[str] tags: The tags (labels) applied to the given entity.
    """
    pulumi.log.warn("""get_hosts is deprecated: xenorchestra.index/gethosts.getHosts has been deprecated in favor of xenorchestra.index/getxoahosts.getXoaHosts""")
    __args__ = dict()
    __args__['poolId'] = pool_id
    __args__['sortBy'] = sort_by
    __args__['sortOrder'] = sort_order
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('xenorchestra:index/getHosts:getHosts', __args__, opts=opts, typ=GetHostsResult).value

    return AwaitableGetHostsResult(
        hosts=pulumi.get(__ret__, 'hosts'),
        id=pulumi.get(__ret__, 'id'),
        master=pulumi.get(__ret__, 'master'),
        pool_id=pulumi.get(__ret__, 'pool_id'),
        sort_by=pulumi.get(__ret__, 'sort_by'),
        sort_order=pulumi.get(__ret__, 'sort_order'),
        tags=pulumi.get(__ret__, 'tags'))
def get_hosts_output(pool_id: Optional[pulumi.Input[str]] = None,
                     sort_by: Optional[pulumi.Input[Optional[str]]] = None,
                     sort_order: Optional[pulumi.Input[Optional[str]]] = None,
                     tags: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetHostsResult]:
    """
    Use this data source to filter Xenorchestra hosts by certain criteria (name_label, tags) for use in other resources.


    :param str pool_id: The pool id used to filter the resulting hosts by.
    :param str sort_by: The host field to sort the results by (id and name_label are supported).
    :param str sort_order: Valid options are `asc` or `desc` and sort order is applied to `sort_by` argument.
    :param Sequence[str] tags: The tags (labels) applied to the given entity.
    """
    pulumi.log.warn("""get_hosts is deprecated: xenorchestra.index/gethosts.getHosts has been deprecated in favor of xenorchestra.index/getxoahosts.getXoaHosts""")
    __args__ = dict()
    __args__['poolId'] = pool_id
    __args__['sortBy'] = sort_by
    __args__['sortOrder'] = sort_order
    __args__['tags'] = tags
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('xenorchestra:index/getHosts:getHosts', __args__, opts=opts, typ=GetHostsResult)
    return __ret__.apply(lambda __response__: GetHostsResult(
        hosts=pulumi.get(__response__, 'hosts'),
        id=pulumi.get(__response__, 'id'),
        master=pulumi.get(__response__, 'master'),
        pool_id=pulumi.get(__response__, 'pool_id'),
        sort_by=pulumi.get(__response__, 'sort_by'),
        sort_order=pulumi.get(__response__, 'sort_order'),
        tags=pulumi.get(__response__, 'tags')))
