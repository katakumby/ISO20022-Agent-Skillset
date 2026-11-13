---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.9 RelatedParties <RltdPties>", "2.4.2.15.18.2.9.8 TradingParty <TradgPty>", "2.4.2.15.18.2.9.8.2 Agent <Agt>"]
file_pages: [147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.9.8.2 Agent <Agt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 147 to 147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 147

```text
Party <Pty> contains the following elements (see "PartyIdentification272" on page 859 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 860
   PostalAddress <PstlAdr> [0..1] ± 861
   Identification <Id> [0..1]  861
{Or     OrganisationIdentification <OrgId> [1..1]  862
       AnyBIC <AnyBIC> [0..1] IdentifierSet C2 863
       LEI <LEI> [0..1] IdentifierSet 863
       Other <Othr> [0..*]  863
         Identification <Id> [1..1] Text 864
         SchemeName <SchmeNm> [0..1]  864
{Or           Code <Cd> [1..1] CodeSet 864
Or}           Proprietary <Prtry> [1..1] Text 864
         Issuer <Issr> [0..1] Text 864
Or}     PrivateIdentification <PrvtId> [1..1]  864
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  865
         BirthDate <BirthDt> [1..1] Date 865
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 865
         CityOfBirth <CityOfBirth> [1..1] Text 866
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C4 866
       Other <Othr> [0..*]  866
         Identification <Id> [1..1] Text 866
         SchemeName <SchmeNm> [0..1]  866
{Or           Code <Cd> [1..1] CodeSet 867
Or}           Proprietary <Prtry> [1..1] Text 867
         Issuer <Issr> [0..1] Text 867
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C4 867
   ContactDetails <CtctDtls> [0..1] ± 867
2.4.2.15.18.2.9.8.2  Agent <Agt>
Presence: [1..1]
Definition: Identification of a financial institution.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
147 March 2026
```

