---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>", "3.4.2.15.18.2.26.2 POI <POI>", "3.4.2.15.18.2.26.2.1 Identification <Id>"]
file_pages: [501]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26.2.1 Identification <Id>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 501 to 501.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 501

```text
POI <POI> contains the following PointOfInteraction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 501
   SystemName <SysNm> [0..1] Text 502
   GroupIdentification <GrpId> [0..1] Text 502
   Capabilities <Cpblties> [0..1]  502
     CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 502
     CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 503
     OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 503
     DisplayCapabilities <DispCpblties> [0..*]  504
       DisplayType <DispTp> [1..1] CodeSet 504
       NumberOfLines <NbOfLines> [1..1] Text 504
       LineWidth <LineWidth> [1..1] Text 504
     PrintLineWidth <PrtLineWidth> [0..1] Text 504
   Component <Cmpnt> [0..*]  504
     POIComponentType <POICmpntTp> [1..1] CodeSet 505
     ManufacturerIdentification <ManfctrId> [0..1] Text 505
     Model <Mdl> [0..1] Text 505
     VersionNumber <VrsnNb> [0..1] Text 505
     SerialNumber <SrlNb> [0..1] Text 506
     ApprovalNumber <ApprvlNb> [0..*] Text 506
3.4.2.15.18.2.26.2.1  Identification <Id>
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
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
501 March 2026
```

