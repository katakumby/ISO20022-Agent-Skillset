---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks"]
file_pages: [1324]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1324 to 1324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1324

```text
C44 TaxFreeCashAndValueRule
If TaxFreeCashProtection is "true" or "1" (Yes), then TaxFreeCashAmount and
ValueOfPensionPolicyOrPlanOrScheme must be present.
If TaxFreeCashProtection is "false" or "0" (Yes), then TaxFreeCashAmount and
ValueOfPensionPolicyOrPlanOrScheme may be present.
C45 TotalAmountYearToDateRule
TotalAmountYearToDate must be equal to the sum of EquityComponent and CashComponent
if present.
C46 TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
C47 TransferScopeTrancheIdentification1Rule
If TransferScope/Code/SDDT (DrawdownTranche) is not present, then
DrawdownTrancheIdentification is not allowed.
If TransferScope/Code/SDDT (DrawdownTranche) is present, then
DrawdownTrancheIdentification may be present.
38.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
38.4.1 MessageReference <MsgRef>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageReference <MsgRef> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
38.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1324 May 2026
```

