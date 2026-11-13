---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["34 camt.102.001.03 CreateStandingOrderV03", "34.4 Message Building Blocks", "34.4.3 ValueSet <ValSet>", "34.4.3.6 ExecutionType <ExctnTp>"]
file_pages: [763]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.102.001.03"]
---

# 34.4.3.6 ExecutionType <ExctnTp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 763 to 763.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 763

```text
DebtorAccount <DbtrAcct> contains the following elements (see "CashAccount40" on page 783 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 783
   Type <Tp> [0..1] ± 783
   Currency <Ccy> [0..1] CodeSet C1 784
   Name <Nm> [0..1] Text 784
   Proxy <Prxy> [0..1] ± 784
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
34.4.3.6  ExecutionType <ExctnTp>
Presence: [0..1]
Definition: Defines whether the standing order is executed through a time-based or an event-based
trigger.
ExecutionType <ExctnTp> contains one of the following ExecutionType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Time <Tm> [1..1] Time 763
Or}   Event <Evt> [1..1]  763
{Or     Code <Cd> [1..1] CodeSet 764
Or}     Proprietary <Prtry> [1..1] Text 764
34.4.3.6.1  Time <Tm>
Presence: [1..1]
Definition: Execution type is executed based on a time trigger.
Datatype: "ISOTime" on page 891
34.4.3.6.2  Event <Evt>
Presence: [1..1]
Approved by the Payments SEG on 04 February 2025 camt.102.001.03 CreateStandingOrderV03
Cash Management - Maintenance 2024 - 2025 763 February 2025
```

