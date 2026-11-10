---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["32 camt.071.001.05 DeleteStandingOrderV05", "32.4 Message Building Blocks", "32.4.2 StandingOrderDetails <StgOrdrDtls>", "32.4.2.2 AllStandingOrders <AllStgOrdrs>"]
file_pages: [742]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.071.001.05"]
---

# 32.4.2.2 AllStandingOrders <AllStgOrdrs>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 742 to 742.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 742

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
32.4.2.2  AllStandingOrders <AllStgOrdrs>
Presence: [1..*]
Definition: Identification of all standing orders defined with specific characteristics.
AllStandingOrders <AllStgOrdrs> contains the following StandingOrderIdentification9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Account <Acct> [1..1] ± C6, C5 742
   AccountOwner <AcctOwnr> [0..1] ± 743
32.4.2.2.1  Account <Acct>
Presence: [1..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Impacted by: C6 "IdentificationOrProxyPresenceRule", C5 "IdentificationAndProxyGuideline"
Approved by the Payments SEG on 04 February 2025 camt.071.001.05 DeleteStandingOrderV05
Cash Management - Maintenance 2024 - 2025 742 February 2025
```

