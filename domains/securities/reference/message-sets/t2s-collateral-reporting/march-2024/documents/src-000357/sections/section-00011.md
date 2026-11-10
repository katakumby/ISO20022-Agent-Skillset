---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 colr.001.001.02 CollateralValueQueryV02", "2.4 Message Building Blocks", "2.4.2 CollateralValueQueryDefinition <CollValQryDef>", "2.4.2.2 NewCriteria <NewCrit>", "2.4.2.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2.3 CashAccountOwner <CshAcctOwnr>"]
file_pages: [11]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 2.4.2.2.2.3 CashAccountOwner <CshAcctOwnr>

Source: [src-000357](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 11 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 11

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
2.4.2.2.2.3  CashAccountOwner <CshAcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account being queried.
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 64 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 64
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 64
2.4.2.2.2.4  CashAccountServicer <CshAcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, which is being queried.
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 46 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  47
     BICFI <BICFI> [0..1] IdentifierSet C4 47
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 48
     LEI <LEI> [0..1] IdentifierSet 48
     Name <Nm> [0..1] Text 48
     PostalAddress <PstlAdr> [0..1] ± 48
     Other <Othr> [0..1] ± 49
   BranchIdentification <BrnchId> [0..1]  50
     Identification <Id> [0..1] Text 50
     LEI <LEI> [0..1] IdentifierSet 50
     Name <Nm> [0..1] Text 50
     PostalAddress <PstlAdr> [0..1] ± 50
2.4.2.2.2.5  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..*]
Definition: ISIN identification of the related financial instrument into which this security can be
converted.
Impacted by: C6 "DescriptionPresenceRule", C7 "DescriptionUsageRule", C9 "ISINGuideline", C10
"ISINPresenceRule", C11 "OtherIdentificationPresenceRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.001.001.02 CollateralValueQueryV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
11 March 2024
```

