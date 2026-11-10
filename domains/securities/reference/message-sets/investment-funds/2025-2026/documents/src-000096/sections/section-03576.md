---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.11 Notification2", "66.1.28.11.1 NotificationType <NtfctnTp>"]
file_pages: [4826]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.11.1 NotificationType <NtfctnTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4826 to 4826.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4826

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NotificationType <NtfctnTp> [1..1] Text 4826
   Required <Reqrd> [1..1] Indicator 4826
   DistributionType <DstrbtnTp> [0..1] ± 4826
66.1.28.11.1  NotificationType <NtfctnTp>
Presence: [1..1]
Definition: Type of notification.
Datatype: "Max35Text" on page 5403
66.1.28.11.2  Required <Reqrd>
Presence: [1..1]
Definition: Indicates whether the notification is required.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.11.3  DistributionType <DstrbtnTp>
Presence: [0..1]
Definition: Specifies how the notification is sent.
DistributionType <DstrbtnTp> contains one of the following elements (see
"InformationDistribution1Choice" on page 4958 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4958
Or}   Proprietary <Prtry> [1..1] ± 4958
66.1.28.12  FundCashOutBreakdown3
Definition: Breakdown of cash movements out of a fund as a result of investment funds transactions,
eg, redemptions or switch-out.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4826 May 2026
```

