---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.2 Warrant <Warrt>", "28.4.2.1.2.1.2.1 Multiplier <Mltplr>"]
file_pages: [1214]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.2.1 Multiplier <Mltplr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1214 to 1214.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1214

```text
Warrant <Warrt> contains the following Warrant4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Multiplier <Mltplr> [0..1] Rate 1214
   SubscriptionPrice <SbcptPric> [0..1]  1214
     ValueType <ValTp> [0..1] CodeSet 1215
     Value <Val> [1..1] ± 1215
     PriceType <PricTp> [0..1] CodeSet 1216
   Type <Tp> [0..1]  1216
{Or     Code <Cd> [1..1] CodeSet 1217
Or}     Proprietary <Prtry> [1..1] ± 1217
   WarrantAgent <WarrtAgt> [0..*]  1217
     Name <Nm> [1..1] Text 1218
     Identification <Id> [0..1]  1218
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1218
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1219
     Purpose <Purp> [0..1] Text 1219
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1219
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1219
     RegistrationDate <RegnDt> [0..1] Date 1220
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1220
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1220
     PostalAddress <PstlAdr> [1..5] ± C10 1220
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1220
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1221
28.4.2.1.2.1.2.1  Multiplier <Mltplr>
Presence: [0..1]
Definition: Specifies the ratio or multiply factor used to convert from contracts to shares.
Datatype: "BaseOneRate" on page 3324
28.4.2.1.2.1.2.2  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Pre-determined price at which the holder of a warrant is entitled to buy the underlying
instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1214 August 2026
```

