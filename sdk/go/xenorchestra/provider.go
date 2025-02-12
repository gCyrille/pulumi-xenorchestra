// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package xenorchestra

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/vatesfr/pulumi-xenorchestra/sdk/go/xenorchestra/internal"
)

// The provider type for the xenorchestra package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	// Password for xoa api. Can be set via the XOA_PASSWORD environment variable.
	Password pulumi.StringPtrOutput `pulumi:"password"`
	// If `retryMode` is set, this specifies the duration for which the backoff method will continue retries. Can be set via
	// the `XOA_RETRY_MAX_TIME` environment variable
	RetryMaxTime pulumi.StringPtrOutput `pulumi:"retryMaxTime"`
	// Specifies if retries should be attempted for requests that require eventual . Can be set via the XOA_RETRY_MODE
	// environment variable.
	RetryMode pulumi.StringPtrOutput `pulumi:"retryMode"`
	// Password for xoa api. Can be set via the XOA_TOKEN environment variable.
	Token pulumi.StringPtrOutput `pulumi:"token"`
	// Hostname of the xoa router. Can be set via the XOA_URL environment variable.
	Url pulumi.StringOutput `pulumi:"url"`
	// User account for xoa api. Can be set via the XOA_USER environment variable.
	Username pulumi.StringPtrOutput `pulumi:"username"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Url == nil {
		return nil, errors.New("invalid value for required argument 'Url'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:xenorchestra", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// Whether SSL should be verified or not. Can be set via the XOA_INSECURE environment variable.
	Insecure *bool `pulumi:"insecure"`
	// Password for xoa api. Can be set via the XOA_PASSWORD environment variable.
	Password *string `pulumi:"password"`
	// If `retryMode` is set, this specifies the duration for which the backoff method will continue retries. Can be set via
	// the `XOA_RETRY_MAX_TIME` environment variable
	RetryMaxTime *string `pulumi:"retryMaxTime"`
	// Specifies if retries should be attempted for requests that require eventual . Can be set via the XOA_RETRY_MODE
	// environment variable.
	RetryMode *string `pulumi:"retryMode"`
	// Password for xoa api. Can be set via the XOA_TOKEN environment variable.
	Token *string `pulumi:"token"`
	// Hostname of the xoa router. Can be set via the XOA_URL environment variable.
	Url string `pulumi:"url"`
	// User account for xoa api. Can be set via the XOA_USER environment variable.
	Username *string `pulumi:"username"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// Whether SSL should be verified or not. Can be set via the XOA_INSECURE environment variable.
	Insecure pulumi.BoolPtrInput
	// Password for xoa api. Can be set via the XOA_PASSWORD environment variable.
	Password pulumi.StringPtrInput
	// If `retryMode` is set, this specifies the duration for which the backoff method will continue retries. Can be set via
	// the `XOA_RETRY_MAX_TIME` environment variable
	RetryMaxTime pulumi.StringPtrInput
	// Specifies if retries should be attempted for requests that require eventual . Can be set via the XOA_RETRY_MODE
	// environment variable.
	RetryMode pulumi.StringPtrInput
	// Password for xoa api. Can be set via the XOA_TOKEN environment variable.
	Token pulumi.StringPtrInput
	// Hostname of the xoa router. Can be set via the XOA_URL environment variable.
	Url pulumi.StringInput
	// User account for xoa api. Can be set via the XOA_USER environment variable.
	Username pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

// Password for xoa api. Can be set via the XOA_PASSWORD environment variable.
func (o ProviderOutput) Password() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Password }).(pulumi.StringPtrOutput)
}

// If `retryMode` is set, this specifies the duration for which the backoff method will continue retries. Can be set via
// the `XOA_RETRY_MAX_TIME` environment variable
func (o ProviderOutput) RetryMaxTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.RetryMaxTime }).(pulumi.StringPtrOutput)
}

// Specifies if retries should be attempted for requests that require eventual . Can be set via the XOA_RETRY_MODE
// environment variable.
func (o ProviderOutput) RetryMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.RetryMode }).(pulumi.StringPtrOutput)
}

// Password for xoa api. Can be set via the XOA_TOKEN environment variable.
func (o ProviderOutput) Token() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Token }).(pulumi.StringPtrOutput)
}

// Hostname of the xoa router. Can be set via the XOA_URL environment variable.
func (o ProviderOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringOutput { return v.Url }).(pulumi.StringOutput)
}

// User account for xoa api. Can be set via the XOA_USER environment variable.
func (o ProviderOutput) Username() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Username }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}
