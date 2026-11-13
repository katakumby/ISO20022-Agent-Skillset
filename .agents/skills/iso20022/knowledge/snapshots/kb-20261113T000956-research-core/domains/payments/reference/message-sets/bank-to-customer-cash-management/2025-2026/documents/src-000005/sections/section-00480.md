---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.5 Invoicee <Invcee>"]
file_pages: [707]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.5 Invoicee <Invcee>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 707 to 707.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 707

```text
Invoicer <Invcr> contains the following elements (see "PartyIdentification272" on page 859 for
details)
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
4.4.2.14.18.2.15.2.5  Invoicee <Invcee>
Presence: [0..1]
Definition: Identification of the party to whom an invoice is issued, when it is different from the debtor or
ultimate debtor.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
707 March 2026
```

