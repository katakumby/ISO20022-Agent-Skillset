---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.9 RelatedTransaction <RltdTx>", "6.4.6.11.4.9.3 TransactionDetails <TxDtls>", "6.4.6.11.4.9.3.11 PostingAmount <PstngAmt>"]
file_pages: [236]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.9.3.11 PostingAmount <PstngAmt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 236 to 236.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 236

```text
CashAccountOwner <CshAcctOwnr> contains the following elements (see "PartyIdentification272"
on page 421 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 422
   PostalAddress <PstlAdr> [0..1] ± 423
   Identification <Id> [0..1]  423
{Or     OrganisationIdentification <OrgId> [1..1]  424
       AnyBIC <AnyBIC> [0..1] IdentifierSet C2 425
       LEI <LEI> [0..1] IdentifierSet 425
       Other <Othr> [0..*]  425
         Identification <Id> [1..1] Text 426
         SchemeName <SchmeNm> [0..1]  426
{Or           Code <Cd> [1..1] CodeSet 426
Or}           Proprietary <Prtry> [1..1] Text 426
         Issuer <Issr> [0..1] Text 426
Or}     PrivateIdentification <PrvtId> [1..1]  426
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  427
         BirthDate <BirthDt> [1..1] Date 427
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 427
         CityOfBirth <CityOfBirth> [1..1] Text 428
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 428
       Other <Othr> [0..*]  428
         Identification <Id> [1..1] Text 428
         SchemeName <SchmeNm> [0..1]  428
{Or           Code <Cd> [1..1] CodeSet 429
Or}           Proprietary <Prtry> [1..1] Text 429
         Issuer <Issr> [0..1] Text 429
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C3 429
   ContactDetails <CtctDtls> [0..1] ± 429
6.4.6.11.4.9.3.11  PostingAmount <PstngAmt>
Presence: [0..1]
Definition: Amount of money that is to be/was posted to the account.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 236 March 2026
```

