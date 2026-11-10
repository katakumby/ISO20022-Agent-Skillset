---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["24 colr.001.001.02 CollateralValueQueryV02", "24.4 Message Building Blocks", "24.4.2 CollateralValueQueryDefinition <CollValQryDef>", "24.4.2.2 NewCriteria <NewCrit>", "24.4.2.2.2 SearchCriteria <SchCrit>", "24.4.2.2.2.3 CashAccountOwner <CshAcctOwnr>"]
file_pages: [585]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 24.4.2.2.2.3 CashAccountOwner <CshAcctOwnr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 585 to 585.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 585

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
24.4.2.2.2.3  CashAccountOwner <CshAcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account being queried.
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
24.4.2.2.2.4  CashAccountServicer <CshAcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, which is being queried.
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 2919 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  2920
     BICFI <BICFI> [0..1] IdentifierSet C3 2920
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 2920
     LEI <LEI> [0..1] IdentifierSet 2920
     Name <Nm> [0..1] Text 2921
     PostalAddress <PstlAdr> [0..1] ± 2921
     Other <Othr> [0..1] ± 2921
   BranchIdentification <BrnchId> [0..1]  2922
     Identification <Id> [0..1] Text 2922
     LEI <LEI> [0..1] IdentifierSet 2922
     Name <Nm> [0..1] Text 2922
     PostalAddress <PstlAdr> [0..1] ± 2923
24.4.2.2.2.5  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..*]
Definition: ISIN identification of the related financial instrument into which this security can be
converted.
Impacted by: C6 "DescriptionPresenceRule", C7 "DescriptionUsageRule", C9 "ISINGuideline", C10
"ISINPresenceRule", C11 "OtherIdentificationPresenceRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.001.001.02 CollateralValueQueryV02
Target2-Securities 585 August 2026
```

