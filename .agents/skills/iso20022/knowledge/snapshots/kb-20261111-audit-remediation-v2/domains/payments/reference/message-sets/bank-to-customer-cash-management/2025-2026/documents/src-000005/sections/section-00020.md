---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.12 Interest <Intrst>"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.12 Interest <Intrst>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
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
2.4.2.12  Interest <Intrst>
Presence: [0..*]
Definition: Provides general interest information that applies to the account at a particular moment in
time.
Interest <Intrst> contains the following AccountInterest4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  49
{Or     Code <Cd> [1..1] CodeSet 50
Or}     Proprietary <Prtry> [1..1] Text 50
   Rate <Rate> [0..*]  50
     Type <Tp> [1..1] ± 50
     ValidityRange <VldtyRg> [0..1] ± 50
   FromToDate <FrToDt> [0..1] ± 51
   Reason <Rsn> [0..1] Text 51
   Tax <Tax> [0..1]  51
     Identification <Id> [0..1] Text 51
     Rate <Rate> [0..1] Rate 52
     Amount <Amt> [0..1] Amount C2, C6 52
2.4.2.12.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of interest.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
49 March 2026
```

