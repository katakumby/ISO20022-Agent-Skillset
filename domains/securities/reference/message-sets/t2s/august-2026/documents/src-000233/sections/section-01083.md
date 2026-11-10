---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.3.2.52 Depository <Dpstry>"]
file_pages: [1554]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.2.52 Depository <Dpstry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1554 to 1554.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1554

```text
SecondaryCommunicationAddress <ScndryComAdr> contains the following elements (see
"CommunicationAddress3" on page 3100 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 3100
   Phone <Phne> [0..1] Text 3100
   Mobile <Mob> [0..1] Text 3101
   FaxNumber <FaxNb> [0..1] Text 3101
   TelexAddress <TlxAdr> [0..1] Text 3101
   URLAddress <URLAdr> [0..1] Text 3101
28.4.2.1.3.2.52  Depository <Dpstry>
Presence: [0..1]
Definition: Entity appointed by the relevant clearing system as a depository for instruments issued in
global or definitive form. The depository keeps the securities for safekeeping purposes on behalf of the
clearing system(s).
Depository <Dpstry> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 1554
   Identification <Id> [0..1]  1555
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1555
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1555
   Purpose <Purp> [0..1] Text 1555
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1556
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1556
   RegistrationDate <RegnDt> [0..1] Date 1556
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 1556
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1556
   PostalAddress <PstlAdr> [1..5] ± C10 1556
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1557
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1557
28.4.2.1.3.2.52.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1554 August 2026
```

