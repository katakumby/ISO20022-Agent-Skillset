---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.2 POI <POI>", "4.4.2.14.18.2.26.2.1 Identification <Id>"]
file_pages: [759]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.2.1 Identification <Id>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 759 to 759.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 759

```text
POI <POI> contains the following PointOfInteraction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 759
   SystemName <SysNm> [0..1] Text 760
   GroupIdentification <GrpId> [0..1] Text 760
   Capabilities <Cpblties> [0..1]  760
     CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 760
     CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 761
     OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 761
     DisplayCapabilities <DispCpblties> [0..*]  762
       DisplayType <DispTp> [1..1] CodeSet 762
       NumberOfLines <NbOfLines> [1..1] Text 762
       LineWidth <LineWidth> [1..1] Text 762
     PrintLineWidth <PrtLineWidth> [0..1] Text 762
   Component <Cmpnt> [0..*]  762
     POIComponentType <POICmpntTp> [1..1] CodeSet 763
     ManufacturerIdentification <ManfctrId> [0..1] Text 763
     Model <Mdl> [0..1] Text 763
     VersionNumber <VrsnNb> [0..1] Text 763
     SerialNumber <SrlNb> [0..1] Text 764
     ApprovalNumber <ApprvlNb> [0..*] Text 764
4.4.2.14.18.2.26.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the POI (Point Of Interaction) for the acquirer or its agent.
Identification <Id> contains the following elements (see "GenericIdentification32" on page 839 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 840
   Type <Tp> [0..1] CodeSet 840
   Issuer <Issr> [0..1] CodeSet 840
   ShortName <ShrtNm> [0..1] Text 841
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
759 March 2026
```

