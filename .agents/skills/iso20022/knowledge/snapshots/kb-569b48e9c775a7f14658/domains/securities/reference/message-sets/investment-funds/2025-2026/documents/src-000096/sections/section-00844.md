---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.3 Pension <Pnsn>", "36.4.15.5.3.1 Identification <Id>"]
file_pages: [1171]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.3.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1171 to 1171.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1171

```text
Following Must be True
    /RingFencedDrawdownAssets Must be absent
• RingFencedDrawdownAssets2Rule
If DrawdownStatus/Code/PART (Partial) or FULL (Full) is present, then
RingFencedDrawdownAssets must be present.
On Condition
    /DrawdownStatus/Code is equal to value 'Partial'
 Or    /DrawdownStatus/Code is equal to value 'Full'
Following Must be True
    /RingFencedDrawdownAssets Must be present
• TaxFreeCashAmountRule
If TaxFreeCashProtection is "false" or "0" (No), then TaxFreeCashAmount is not allowed.
If TaxFreeCashProtection is "true" or "1" (Yes), then TaxFreeCashAmount may be present.
On Condition
    /TaxFreeCashProtection is equal to value 'false'
 Or    /TaxFreeCashProtection is equal to value '0'
Following Must be True
    /TaxFreeCashAmount Must be absent
• TaxFreeCashAndValueRule
If TaxFreeCashProtection is "true" or "1" (Yes), then TaxFreeCashAmount and
ValueOfPensionPolicyOrPlanOrScheme must be present.
If TaxFreeCashProtection is "false" or "0" (Yes), then TaxFreeCashAmount and
ValueOfPensionPolicyOrPlanOrScheme may be present.
On Condition
    /TaxFreeCashProtection is equal to value 'true'
 Or    /TaxFreeCashProtection is equal to value '1'
Following Must be True
    /TaxFreeCashAmount Must be present
 And    /ValueOfPensionPolicyOrPlanOrScheme Must be present
• TransferScopeTrancheIdentification1Rule
If TransferScope/Code/SDDT (DrawdownTranche) is not present, then
DrawdownTrancheIdentification is not allowed.
If TransferScope/Code/SDDT (DrawdownTranche) is present, then DrawdownTrancheIdentification
may be present.
On Condition
    /TransferScope/Code is different from value 'DrawdownTranche'
Following Must be True
    /DrawdownTrancheIdentification Must be absent
36.4.15.5.3.1  Identification <Id>
Presence: [0..1]
Definition: Identification of the pension policy, plan or scheme.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1171 May 2026
```

