---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.1 PaymentCommonInformation <PmtCmonInf>", "5.4.2.1.1.2 PaymentTo <PmtTo>"]
file_pages: [235]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.1.2 PaymentTo <PmtTo>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 235 to 235.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 235

```text
5.4.2.1.1.2  PaymentTo <PmtTo>
Presence: [0..1]
Definition: Destination of the payment (be it a member or a system or both).
PaymentTo <PmtTo> contains the following System3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..1] ± 235
   MemberIdentification <MmbId> [0..1] ± 235
   Country <Ctry> [0..1] CodeSet C5 236
   AccountIdentification <AcctId> [0..1] ± 236
5.4.2.1.1.2.1  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"MarketInfrastructureIdentification1Choice" on page 822 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 823
Or}   Proprietary <Prtry> [1..1] Text 823
5.4.2.1.1.2.2  MemberIdentification <MmbId>
Presence: [0..1]
Definition: Unique and unambiguous identification of a member within a system, assigned using the
member identification scheme of the system.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 235 February 2025
```

