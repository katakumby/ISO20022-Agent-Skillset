---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.12 Interest <Intrst>"]
file_pages: [568]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.12 Interest <Intrst>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 568 to 568.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 568

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
4.4.2.12  Interest <Intrst>
Presence: [0..*]
Definition: Provides general interest information that applies to the account at a particular moment in
time.
Interest <Intrst> contains the following AccountInterest4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  568
{Or     Code <Cd> [1..1] CodeSet 569
Or}     Proprietary <Prtry> [1..1] Text 569
   Rate <Rate> [0..*]  569
     Type <Tp> [1..1] ± 569
     ValidityRange <VldtyRg> [0..1] ± 569
   FromToDate <FrToDt> [0..1] ± 570
   Reason <Rsn> [0..1] Text 570
   Tax <Tax> [0..1]  570
     Identification <Id> [0..1] Text 570
     Rate <Rate> [0..1] Rate 571
     Amount <Amt> [0..1] Amount C2, C6 571
4.4.2.12.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of interest.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
568 March 2026
```

