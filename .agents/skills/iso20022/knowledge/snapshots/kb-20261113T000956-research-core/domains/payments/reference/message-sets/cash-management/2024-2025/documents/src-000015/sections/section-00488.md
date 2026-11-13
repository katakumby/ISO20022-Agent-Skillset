---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["25 camt.047.001.08 ReturnReservationV08", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.2 DefaultReservation <DfltRsvatn>", "25.4.2.1.2.1 ReservationIdentification <RsvatnId>", "25.4.2.1.2.1.5 AccountIdentification <AcctId>"]
file_pages: [650]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.047.001.08"]
---

# 25.4.2.1.2.1.5 AccountIdentification <AcctId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 650 to 650.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 650

```text
AccountOwner <AcctOwnr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 803 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  804
     BICFI <BICFI> [0..1] IdentifierSet C2 804
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 805
     LEI <LEI> [0..1] IdentifierSet 805
     Name <Nm> [0..1] Text 805
     PostalAddress <PstlAdr> [0..1] ± 805
     Other <Othr> [0..1] ± 806
   BranchIdentification <BrnchId> [0..1]  807
     Identification <Id> [0..1] Text 807
     LEI <LEI> [0..1] IdentifierSet 807
     Name <Nm> [0..1] Text 807
     PostalAddress <PstlAdr> [0..1] ± 807
25.4.2.1.2.1.5  AccountIdentification <AcctId>
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
25.4.2.1.2.2  ReservationOrError <RsvatnOrErr>
Presence: [1..1]
Definition: Requested information on the limit.
Approved by the Payments SEG on 04 February 2025 camt.047.001.08 ReturnReservationV08
Cash Management - Maintenance 2024 - 2025 650 February 2025
```

