---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.1 SecurityStatus <SctySts>"]
file_pages: [330]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.1 SecurityStatus <SctySts>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 330 to 330.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 330

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 393
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 393
     PostalAddress <PstlAdr> [1..5] ± C10 393
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 393
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 394
   UnderlyingRisk <UndrlygRsk> [0..1]  394
     Name <Nm> [1..1] Text 395
     Identification <Id> [0..1]  395
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 395
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 396
     Purpose <Purp> [0..1] Text 396
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 396
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 396
     RegistrationDate <RegnDt> [0..1] Date 397
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 397
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 397
     PostalAddress <PstlAdr> [1..5] ± C10 397
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 397
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 398
   SecurityCSDLink <SctyCSDLk> [0..*]  398
     ValidFrom <VldFr> [1..1] ± 399
     ValidTo <VldTo> [0..1] ± 399
     SecurityMaintenance <SctyMntnc> [0..1] Indicator 399
     IssuerCSD <IssrCSD> [0..1] ± 400
     InvestorCSD <InvstrCSD> [0..1] ± 400
     TechnicalIssuerCSD <TechIssrCSD> [0..1] ± 400
     IssuanceAccount <IssncAcct> [0..*]  400
       IssuanceAccount <IssncAcct> [1..1] ± 401
       PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 401
13.1.6.3.1  SecurityStatus <SctySts>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 330 March 2024
```

