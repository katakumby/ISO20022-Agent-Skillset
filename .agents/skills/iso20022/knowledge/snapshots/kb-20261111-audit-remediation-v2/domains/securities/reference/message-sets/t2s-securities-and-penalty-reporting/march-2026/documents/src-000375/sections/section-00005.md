---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["2 semt.025.001.01 SecuritiesAccountPositionQueryV01", "2.2 Structure"]
file_pages: [6]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 2.2 Structure

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 6 to 6.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 6

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctPosQry> [1..1]  
   Statement <Stmt> [1..1] ± 7
   SearchCriteria <SchCrit> [1..1]  7
     AccountOwner <AcctOwnr> [0..1] ± 8
     AccountServicer <AcctSvcr> [0..1] ± 8
     SafekeepingAccount <SfkpgAcct> [0..1] ± 8
     FinancialInstrument <FinInstrm> [0..1] ± C4, C5,
C7, C8,
C9
9
     CountryOfIssue <CtryOfIsse> [0..1] CodeSet C3 10
     SubBalanceType <SubBalTp> [0..1] ± 10
     ReturnZeroPosition <RtrZeroPos> [1..1] Indicator 10
     OtherBusinessParties <OthrBizPties> [0..1]  11
       Investor <Invstr> [0..*] ± C6, C10,
C11
11
   SupplementaryData <SplmtryData> [0..*] ± C12 12
2.3 Constraints
C1 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C5 DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG 19 February 2026. semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities - Securities and Penalty Reporting 6 March 2026
```

