---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["33 camt.101.001.02 CreateLimitV02", "33.4 Message Building Blocks", "33.4.2 LimitData <LmtData>", "33.4.2.1 LimitIdentification <LmtId>", "33.4.2.1.3 Type <Tp>", "33.4.2.1.3.2 Proprietary <Prtry>"]
file_pages: [752]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.101.001.02"]
---

# 33.4.2.1.3.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 752 to 752.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 752

```text
CodeName Name Definition
securities that are being purchased
("collateral flows").
EXGT ExternalGuarantee Limit is related to a cap amount granted
by a national central bank or a
settlement bank.
33.4.2.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of the limit, in a proprietary form.
Datatype: "Max35Text" on page 889
33.4.2.1.4  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Owner of the account which is being queried.
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
33.4.2.1.5  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Approved by the Payments SEG on 04 February 2025 camt.101.001.02 CreateLimitV02
Cash Management - Maintenance 2024 - 2025 752 February 2025
```

