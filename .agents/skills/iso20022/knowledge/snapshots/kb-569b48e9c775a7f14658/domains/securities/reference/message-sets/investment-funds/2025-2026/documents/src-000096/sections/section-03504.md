---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.13 InvestmentFundOrder4"]
file_pages: [4754]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.13 InvestmentFundOrder4

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4754 to 4754.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4754

```text
Other <Othr> contains the following elements (see "OtherDistributionStrategy1" on page 4773 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DistributionStrategyType <DstrbtnStrtgyTp> [0..1] Text 4773
   Target <Trgt> [0..1] ± 4774
   AdditionalInformation <AddtlInf> [0..1] ± 4774
66.1.26.13  InvestmentFundOrder4
Definition: Identifies an order linked to an account opening.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderReference <OrdrRef> [0..1] Text 4754
   MasterReference <MstrRef> [0..1] Text 4754
66.1.26.13.1  OrderReference <OrdrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
66.1.26.13.2  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
66.1.26.14  MoneyPurchaseAnnualAllowance1
Definition: Information about a Money Purchase Annual Allowance (MPAA).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Triggered <Trggrd> [1..1] Indicator 4754
   TriggeredDate <TrggrdDt> [0..1] Date 4755
66.1.26.14.1  Triggered <Trggrd>
Presence: [1..1]
Definition: Indicates whether the annual allowance has been triggered.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4754 May 2026
```

