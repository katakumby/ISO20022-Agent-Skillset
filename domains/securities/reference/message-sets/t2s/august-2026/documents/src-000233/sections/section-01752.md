---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["70 semt.025.001.01 SecuritiesAccountPositionQueryV01", "70.4 Message Building Blocks"]
file_pages: [2403]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 70.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2403 to 2403.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2403

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
70.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
70.4.1 Statement <Stmt>
Presence: [1..1]
Definition: Defines the criteria used to report on the securities account position.
Statement <Stmt> contains the following elements (see "Statement89" on page 3057 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateOrPeriod <DtOrPrd> [0..1] ± 3057
   HistoricData <HstrcData> [1..1] Indicator 3057
   StatementType <StmtTp> [0..1] ± 3057
70.4.2 SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Provides the criteria in the form of business attributes to extract the securities account
position result set.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities 2403 August 2026
```

