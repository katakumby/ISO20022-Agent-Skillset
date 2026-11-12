---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>", "39.4.15.4 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "39.4.15.4.2 Instrument <Instrm>", "39.4.15.4.2.3 OtherAsset <OthrAsst>"]
file_pages: [1475]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.15.4.2.3 OtherAsset <OthrAsst>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1475 to 1475.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1475

```text
CashAsset <CshAsst> contains the following elements (see "CashAsset2" on page 4527 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAssetType <CshAsstTp> [1..1]  4527
{Or     Code <Cd> [1..1] CodeSet 4527
Or}     Proprietary <Prtry> [1..1] ± 4528
   HoldingCurrency <HldgCcy> [1..1] CodeSet C1 4528
   AdditionalInformation <AddtlInf> [0..1] ± 4528
39.4.15.4.2.3  OtherAsset <OthrAsst>
Presence: [1..1]
Definition: Identification of another kind of asset in the holding that is not a security or cash.
OtherAsset <OthrAsst> contains the following elements (see "OtherAsset2" on page 4525 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherAssetType <OthrAsstTp> [1..1]  4525
{Or     Code <Cd> [1..1] CodeSet 4525
Or}     Proprietary <Prtry> [1..1] ± 4526
   Identification <Id> [1..1] Text 4526
   Name <Nm> [0..1] Text 4526
   Description <Desc> [0..1] Text 4526
   OtherIdentification <OthrId> [0..5] Text 4526
   AdditionalInformation <AddtlInf> [0..*] ± 4527
39.4.15.4.3  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the transfer. This reference can typically
be used in a hub scenario to give the reference of the transfer as assigned by the underlying client.
ClientReference <ClntRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
39.4.15.4.4  CounterpartyReference <CtrPtyRef>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1475 May 2026
```

