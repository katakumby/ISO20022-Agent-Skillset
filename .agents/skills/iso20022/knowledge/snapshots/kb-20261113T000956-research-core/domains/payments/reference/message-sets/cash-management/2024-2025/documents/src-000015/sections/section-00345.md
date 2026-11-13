---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.4 Message Building Blocks", "13.4.2 ReportOrError <RptOrErr>", "13.4.2.1 Report <Rpt>", "13.4.2.1.2 MemberOrError <MmbOrErr>", "13.4.2.1.2.1 Member <Mmb>", "13.4.2.1.2.1.3 Account <Acct>"]
file_pages: [489]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.4.2.1.2.1.3 Account <Acct>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 489 to 489.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 489

```text
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 802 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 803
   SchemeName <SchmeNm> [0..1]  803
{Or     Code <Cd> [1..1] CodeSet 803
Or}     Proprietary <Prtry> [1..1] Text 803
   Issuer <Issr> [0..1] Text 803
13.4.2.1.2.1.3  Account <Acct>
Presence: [0..*]
Definition: Account to or from which a cash entry is made.
Impacted by: C6 "IdentificationOrProxyPresenceRule", C5 "IdentificationAndProxyGuideline"
Account <Acct> contains the following elements (see "CashAccount40" on page 783 for details)
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
13.4.2.1.2.1.4  Type <Tp>
Presence: [0..1]
Definition: Nature of the relationship a member has with a system.
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 489 February 2025
```

