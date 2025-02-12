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
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/vatesfr/pulumi-xenorchestra/sdk/go/xenorchestra"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			localStorage, err := xenorchestra.GetXoaStorageRepository(ctx, &xenorchestra.GetXoaStorageRepositoryArgs{
//				NameLabel: "Your storage repository label",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = xenorchestra.NewVm(ctx, "demo-vm", &xenorchestra.VmArgs{
//				Disks: xenorchestra.VmDiskArray{
//					&xenorchestra.VmDiskArgs{
//						SrId:      pulumi.String(localStorage.Id),
//						NameLabel: pulumi.String("Ubuntu Bionic Beaver 18.04_imavo"),
//						Size:      pulumi.Int(32212254720),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// Deprecated: xenorchestra.index/getsr.getSr has been deprecated in favor of xenorchestra.index/getxoastoragerepository.getXoaStorageRepository
func GetSr(ctx *pulumi.Context, args *GetSrArgs, opts ...pulumi.InvokeOption) (*GetSrResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetSrResult
	err := ctx.Invoke("xenorchestra:index/getSr:getSr", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSr.
type GetSrArgs struct {
	// The name of the storage repository to look up
	NameLabel string `pulumi:"nameLabel"`
	// The Id of the pool the storage repository exists on.
	PoolId *string `pulumi:"poolId"`
	// The tags (labels) applied to the given entity.
	Tags []string `pulumi:"tags"`
}

// A collection of values returned by getSr.
type GetSrResult struct {
	// The storage container.
	Container string `pulumi:"container"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the storage repository to look up
	NameLabel string `pulumi:"nameLabel"`
	// The physical storage size.
	PhysicalUsage int `pulumi:"physicalUsage"`
	// The Id of the pool the storage repository exists on.
	PoolId *string `pulumi:"poolId"`
	// The storage size.
	Size int `pulumi:"size"`
	// The type of storage repository (lvm, udev, iso, user, etc).
	SrType string `pulumi:"srType"`
	// The tags (labels) applied to the given entity.
	Tags []string `pulumi:"tags"`
	// The current usage for this storage repository.
	Usage int `pulumi:"usage"`
	// uuid of the storage repository. This is equivalent to the id.
	Uuid string `pulumi:"uuid"`
}

func GetSrOutput(ctx *pulumi.Context, args GetSrOutputArgs, opts ...pulumi.InvokeOption) GetSrResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetSrResultOutput, error) {
			args := v.(GetSrArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("xenorchestra:index/getSr:getSr", args, GetSrResultOutput{}, options).(GetSrResultOutput), nil
		}).(GetSrResultOutput)
}

// A collection of arguments for invoking getSr.
type GetSrOutputArgs struct {
	// The name of the storage repository to look up
	NameLabel pulumi.StringInput `pulumi:"nameLabel"`
	// The Id of the pool the storage repository exists on.
	PoolId pulumi.StringPtrInput `pulumi:"poolId"`
	// The tags (labels) applied to the given entity.
	Tags pulumi.StringArrayInput `pulumi:"tags"`
}

func (GetSrOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSrArgs)(nil)).Elem()
}

// A collection of values returned by getSr.
type GetSrResultOutput struct{ *pulumi.OutputState }

func (GetSrResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSrResult)(nil)).Elem()
}

func (o GetSrResultOutput) ToGetSrResultOutput() GetSrResultOutput {
	return o
}

func (o GetSrResultOutput) ToGetSrResultOutputWithContext(ctx context.Context) GetSrResultOutput {
	return o
}

// The storage container.
func (o GetSrResultOutput) Container() pulumi.StringOutput {
	return o.ApplyT(func(v GetSrResult) string { return v.Container }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetSrResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetSrResult) string { return v.Id }).(pulumi.StringOutput)
}

// The name of the storage repository to look up
func (o GetSrResultOutput) NameLabel() pulumi.StringOutput {
	return o.ApplyT(func(v GetSrResult) string { return v.NameLabel }).(pulumi.StringOutput)
}

// The physical storage size.
func (o GetSrResultOutput) PhysicalUsage() pulumi.IntOutput {
	return o.ApplyT(func(v GetSrResult) int { return v.PhysicalUsage }).(pulumi.IntOutput)
}

// The Id of the pool the storage repository exists on.
func (o GetSrResultOutput) PoolId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSrResult) *string { return v.PoolId }).(pulumi.StringPtrOutput)
}

// The storage size.
func (o GetSrResultOutput) Size() pulumi.IntOutput {
	return o.ApplyT(func(v GetSrResult) int { return v.Size }).(pulumi.IntOutput)
}

// The type of storage repository (lvm, udev, iso, user, etc).
func (o GetSrResultOutput) SrType() pulumi.StringOutput {
	return o.ApplyT(func(v GetSrResult) string { return v.SrType }).(pulumi.StringOutput)
}

// The tags (labels) applied to the given entity.
func (o GetSrResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetSrResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// The current usage for this storage repository.
func (o GetSrResultOutput) Usage() pulumi.IntOutput {
	return o.ApplyT(func(v GetSrResult) int { return v.Usage }).(pulumi.IntOutput)
}

// uuid of the storage repository. This is equivalent to the id.
func (o GetSrResultOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v GetSrResult) string { return v.Uuid }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetSrResultOutput{})
}
