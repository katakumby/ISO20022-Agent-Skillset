---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["2 semt.025.001.01 SecuritiesAccountPositionQueryV01", "2.4 Message Building Blocks"]
file_pages: [7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 2.4 Message Building Blocks

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 7 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
C6 IdentificationNationalityOfInvestorRule
Identification and/or Nationality must be present.
C7 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C8 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C9 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C10 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C11 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C12 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 Statement <Stmt>
Presence: [1..1]
Definition: Defines the criteria used to report on the securities account position.
Statement <Stmt> contains the following elements (see "Statement89" on page 410 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateOrPeriod <DtOrPrd> [0..1] ± 410
   HistoricData <HstrcData> [1..1] Indicator 411
   StatementType <StmtTp> [0..1] ± 411
2.4.2 SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Provides the criteria in the form of business attributes to extract the securities account
position result set.
Approved by the Securities SEG 19 February 2026. semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities - Securities and Penalty Reporting 7 March 2026
```

