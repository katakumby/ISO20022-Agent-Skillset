---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 colr.002.001.02 CollateralValueReportV02", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 BusinessReport <BizRpt>", "3.4.2.1.4 SecuritiesAccountOwner <SctiesAcctOwnr>"]
file_pages: [26]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 3.4.2.1.4 SecuritiesAccountOwner <SctiesAcctOwnr>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 26 to 26.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

```text
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
3.4.2.1.4  SecuritiesAccountOwner <SctiesAcctOwnr>
Presence: [0..1]
Definition: Unique and unambiguous identification of the securities account owner.
SecuritiesAccountOwner <SctiesAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 64 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 64
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 64
3.4.2.1.5  SecuritiesAccountServicer <SctiesAcctSvcr>
Presence: [0..1]
Definition: Party that manages the securities account on behalf of the account owner.
SecuritiesAccountServicer <SctiesAcctSvcr> contains the following elements (see
"PartyIdentification136" on page 62 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 62
   LEI <LEI> [0..1] IdentifierSet 62
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
26 March 2024
```

