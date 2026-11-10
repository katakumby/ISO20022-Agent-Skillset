---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.29 PhysicalDeliveryIndicator <PhysDlvryInd>"]
file_pages: [2870]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.29 PhysicalDeliveryIndicator <PhysDlvryInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2870 to 2870.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2870

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
49.4.5.9.29  PhysicalDeliveryIndicator <PhysDlvryInd>
Presence: [1..1]
Definition: Indicates whether the financial instrument is to be physically delivered.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
49.4.5.9.30  PhysicalDeliveryDetails <PhysDlvryDtls>
Presence: [0..1]
Definition: Information related to the physical delivery of the securities.
PhysicalDeliveryDetails <PhysDlvryDtls> contains the following elements (see
"DeliveryParameters3" on page 5096 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Address <Adr> [1..1] ± 5096
   IssuedCertificateNumber <IssdCertNb> [0..1] Text 5097
49.4.5.9.31  StaffClientBreakdown <StffClntBrkdwn>
Presence: [0..4]
Definition: Breakdown of the net amount per type of order.
StaffClientBreakdown <StffClntBrkdwn> contains the following elements (see
"InvestmentFundsOrderBreakdown2" on page 4733 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderBreakdownType <OrdrBrkdwnTp> [1..1]  4733
{Or     Code <Cd> [1..1] CodeSet 4733
Or}     Proprietary <Prtry> [1..1] ± 4733
   Amount <Amt> [1..1] Amount C1, C13 4734
49.4.5.9.32  Refund <Rfnd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2870 May 2026
```

