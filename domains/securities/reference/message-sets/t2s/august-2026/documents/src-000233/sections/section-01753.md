---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["70 semt.025.001.01 SecuritiesAccountPositionQueryV01", "70.4 Message Building Blocks", "70.4.2 SearchCriteria <SchCrit>", "70.4.2.1 AccountOwner <AcctOwnr>"]
file_pages: [2404]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 70.4.2.1 AccountOwner <AcctOwnr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2404 to 2404.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2404

```text
SearchCriteria <SchCrit> contains the following PositionSearchCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 2404
   AccountServicer <AcctSvcr> [0..1] ± 2404
   SafekeepingAccount <SfkpgAcct> [0..1] ± 2404
   FinancialInstrument <FinInstrm> [0..1] ± C4, C5,
C7, C8,
C9
2405
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C3 2406
   SubBalanceType <SubBalTp> [0..1] ± 2406
   ReturnZeroPosition <RtrZeroPos> [1..1] Indicator 2406
   OtherBusinessParties <OthrBizPties> [0..1]  2407
     Investor <Invstr> [0..*] ± C6, C10,
C11
2407
70.4.2.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
70.4.2.2  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
70.4.2.3  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities 2404 August 2026
```

