---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.8 LegInformation <LegInf>", "56.4.3.3.8.1 LegIdentification <LegId>", "56.4.3.3.8.1.1 RedemptionLegIdentification <RedLegId>"]
file_pages: [4187]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.8.1.1 RedemptionLegIdentification <RedLegId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4187 to 4187.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4187

```text
LegIdentification <LegId> contains one of the following LegIdentification1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RedemptionLegIdentification <RedLegId> [1..1] Text 4187
Or}   SubscriptionLegIdentification <SbcptLegId> [1..1] Text 4187
56.4.3.3.8.1.1  RedemptionLegIdentification <RedLegId>
Presence: [1..1]
Definition: Unique technical identifier for the instance of the leg within a switch.
Datatype: "Max35Text" on page 5403
56.4.3.3.8.1.2  SubscriptionLegIdentification <SbcptLegId>
Presence: [1..1]
Definition: Unique technical identifier for the instance of the leg within a switch.
Datatype: "Max35Text" on page 5403
56.4.3.3.8.2  LegRejectionReason <LegRjctnRsn>
Presence: [0..1]
Definition: Additional information about the reason for the rejection of the leg.
Datatype: "Max350Text" on page 5403
56.4.3.3.8.3  RepairedFee <RprdFee>
Presence: [0..10]
Definition: Elements from the original individual order that have been repaired so that the order can be
accepted.
Impacted by: C6 "CommercialAgreementRule", C12 "FeeElementRule"
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4187 May 2026
```

