---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.1 PaymentTo <PmtTo>", "4.4.2.2.2.2.1.4 AccountIdentification <AcctId>"]
file_pages: [137]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.1.4 AccountIdentification <AcctId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 137 to 137.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 137

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
4.4.2.2.2.2.1.4  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
AccountIdentification <AcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 787 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 787
Or}   Other <Othr> [1..1] ± 788
4.4.2.2.2.2.2  PaymentFrom <PmtFr>
Presence: [0..*]
Definition: Defines the criteria which are used to search for the origin of the payment.
PaymentFrom <PmtFr> contains the following SystemSearch5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..*]  137
{Or     Code <Cd> [1..1] CodeSet 138
Or}     Proprietary <Prtry> [1..1] Text 138
   MemberIdentification <MmbId> [0..*] ± 138
   Country <Ctry> [0..1] CodeSet C5 138
   AccountIdentification <AcctId> [0..1] ± 139
4.4.2.2.2.2.2.1  SystemIdentification <SysId>
Presence: [0..*]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following ClearingSystemIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 138
Or}   Proprietary <Prtry> [1..1] Text 138
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 137 February 2025
```

