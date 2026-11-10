---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.4 Warrant4", "13.1.2.4.1 Multiplier <Mltplr>"]
file_pages: [228]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.4.1 Multiplier <Mltplr>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 228 to 228.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 228

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Multiplier <Mltplr> [0..1] Rate 228
   SubscriptionPrice <SbcptPric> [0..1]  228
     ValueType <ValTp> [0..1] CodeSet 229
     Value <Val> [1..1] ± 229
     PriceType <PricTp> [0..1] CodeSet 230
   Type <Tp> [0..1]  230
{Or     Code <Cd> [1..1] CodeSet 231
Or}     Proprietary <Prtry> [1..1] ± 231
   WarrantAgent <WarrtAgt> [0..*]  231
     Name <Nm> [1..1] Text 232
     Identification <Id> [0..1]  232
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 232
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 233
     Purpose <Purp> [0..1] Text 233
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 233
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 233
     RegistrationDate <RegnDt> [0..1] Date 234
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 234
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 234
     PostalAddress <PstlAdr> [1..5] ± C10 234
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 234
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 235
13.1.2.4.1  Multiplier <Mltplr>
Presence: [0..1]
Definition: Specifies the ratio or multiply factor used to convert from contracts to shares.
Datatype: "BaseOneRate" on page 532
13.1.2.4.2  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Pre-determined price at which the holder of a warrant is entitled to buy the underlying
instrument.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 228 March 2024
```

