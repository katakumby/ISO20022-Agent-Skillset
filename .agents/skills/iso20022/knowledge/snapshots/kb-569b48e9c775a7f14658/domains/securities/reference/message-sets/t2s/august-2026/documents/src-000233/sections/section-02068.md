---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.9 RelatedTransaction <RltdTx>", "81.4.6.11.4.9.3 TransactionDetails <TxDtls>", "81.4.6.11.4.9.3.11 PostingAmount <PstngAmt>"]
file_pages: [2818]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.9.3.11 PostingAmount <PstngAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2818 to 2818.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2818

```text
CashAccountOwner <CshAcctOwnr> contains the following elements (see "PartyIdentification272"
on page 3068 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 3068
   PostalAddress <PstlAdr> [0..1] ± 3069
   Identification <Id> [0..1]  3069
{Or     OrganisationIdentification <OrgId> [1..1]  3070
       AnyBIC <AnyBIC> [0..1] IdentifierSet C2 3071
       LEI <LEI> [0..1] IdentifierSet 3071
       Other <Othr> [0..*]  3071
         Identification <Id> [1..1] Text 3072
         SchemeName <SchmeNm> [0..1]  3072
{Or           Code <Cd> [1..1] CodeSet 3072
Or}           Proprietary <Prtry> [1..1] Text 3072
         Issuer <Issr> [0..1] Text 3072
Or}     PrivateIdentification <PrvtId> [1..1]  3072
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  3073
         BirthDate <BirthDt> [1..1] Date 3073
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 3073
         CityOfBirth <CityOfBirth> [1..1] Text 3074
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 3074
       Other <Othr> [0..*]  3074
         Identification <Id> [1..1] Text 3074
         SchemeName <SchmeNm> [0..1]  3074
{Or           Code <Cd> [1..1] CodeSet 3075
Or}           Proprietary <Prtry> [1..1] Text 3075
         Issuer <Issr> [0..1] Text 3075
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C3 3075
   ContactDetails <CtctDtls> [0..1] ± 3075
81.4.6.11.4.9.3.11  PostingAmount <PstngAmt>
Presence: [0..1]
Definition: Amount of money that is to be/was posted to the account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2818 August 2026
```

