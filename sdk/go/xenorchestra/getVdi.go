// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package xenorchestra

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/vatesfr/pulumi-xenorchestra/sdk/go/xenorchestra/internal"
)

// ## Example Usage
//
// Deprecated: xenorchestra.index/getvdi.getVdi has been deprecated in favor of xenorchestra.index/getxoavdi.getXoaVdi
func LookupVdi(ctx *pulumi.Context, args *LookupVdiArgs, opts ...pulumi.InvokeOption) (*LookupVdiResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupVdiResult
	err := ctx.Invoke("xenorchestra:index/getVdi:getVdi", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVdi.
type LookupVdiArgs struct {
	// The ID of the VDI.
	Id *string `pulumi:"id"`
	// The name of the VDI to look up.
	NameLabel *string `pulumi:"nameLabel"`
	// The ID of the pool the VDI belongs to. This is useful if you have a VDI with the same name on different pools.
	PoolId *string `pulumi:"poolId"`
	// The tags (labels) applied to the given entity.
	Tags []string `pulumi:"tags"`
}

// A collection of values returned by getVdi.
type LookupVdiResult struct {
	// The ID of the VDI.
	Id string `pulumi:"id"`
	// The name of the VDI to look up.
	NameLabel *string `pulumi:"nameLabel"`
	// The ID of the parent VDI if one exists. An example of when a VDI will have a parent is when it was created from a VM fast clone.
	Parent string `pulumi:"parent"`
	// The ID of the pool the VDI belongs to. This is useful if you have a VDI with the same name on different pools.
	PoolId *string `pulumi:"poolId"`
	// The tags (labels) applied to the given entity.
	Tags []string `pulumi:"tags"`
}

func LookupVdiOutput(ctx *pulumi.Context, args LookupVdiOutputArgs, opts ...pulumi.InvokeOption) LookupVdiResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupVdiResultOutput, error) {
			args := v.(LookupVdiArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("xenorchestra:index/getVdi:getVdi", args, LookupVdiResultOutput{}, options).(LookupVdiResultOutput), nil
		}).(LookupVdiResultOutput)
}

// A collection of arguments for invoking getVdi.
type LookupVdiOutputArgs struct {
	// The ID of the VDI.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The name of the VDI to look up.
	NameLabel pulumi.StringPtrInput `pulumi:"nameLabel"`
	// The ID of the pool the VDI belongs to. This is useful if you have a VDI with the same name on different pools.
	PoolId pulumi.StringPtrInput `pulumi:"poolId"`
	// The tags (labels) applied to the given entity.
	Tags pulumi.StringArrayInput `pulumi:"tags"`
}

func (LookupVdiOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVdiArgs)(nil)).Elem()
}

// A collection of values returned by getVdi.
type LookupVdiResultOutput struct{ *pulumi.OutputState }

func (LookupVdiResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVdiResult)(nil)).Elem()
}

func (o LookupVdiResultOutput) ToLookupVdiResultOutput() LookupVdiResultOutput {
	return o
}

func (o LookupVdiResultOutput) ToLookupVdiResultOutputWithContext(ctx context.Context) LookupVdiResultOutput {
	return o
}

// The ID of the VDI.
func (o LookupVdiResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVdiResult) string { return v.Id }).(pulumi.StringOutput)
}

// The name of the VDI to look up.
func (o LookupVdiResultOutput) NameLabel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVdiResult) *string { return v.NameLabel }).(pulumi.StringPtrOutput)
}

// The ID of the parent VDI if one exists. An example of when a VDI will have a parent is when it was created from a VM fast clone.
func (o LookupVdiResultOutput) Parent() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVdiResult) string { return v.Parent }).(pulumi.StringOutput)
}

// The ID of the pool the VDI belongs to. This is useful if you have a VDI with the same name on different pools.
func (o LookupVdiResultOutput) PoolId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVdiResult) *string { return v.PoolId }).(pulumi.StringPtrOutput)
}

// The tags (labels) applied to the given entity.
func (o LookupVdiResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupVdiResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVdiResultOutput{})
}
