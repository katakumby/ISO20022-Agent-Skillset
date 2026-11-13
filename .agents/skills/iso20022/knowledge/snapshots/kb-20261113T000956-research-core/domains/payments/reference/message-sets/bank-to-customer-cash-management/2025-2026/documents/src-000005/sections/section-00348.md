---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>", "3.4.2.15.18.2.26.2 POI <POI>", "3.4.2.15.18.2.26.2.2 SystemName <SysNm>"]
file_pages: [502]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26.2.2 SystemName <SysNm>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 502 to 502.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 502

```text
3.4.2.15.18.2.26.2.2  SystemName <SysNm>
Presence: [0..1]
Definition: Common name assigned by the acquirer to the POI system.
Datatype: "Max70Text" on page 917
3.4.2.15.18.2.26.2.3  GroupIdentification <GrpId>
Presence: [0..1]
Definition: Identifier assigned by the merchant identifying a set of POI terminals performing some
categories of transactions.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.26.2.4  Capabilities <Cpblties>
Presence: [0..1]
Definition: Capabilities of the POI performing the transaction.
Capabilities <Cpblties> contains the following PointOfInteractionCapabilities1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
3.4.2.15.18.2.26.2.4.1  CardReadingCapabilities <CardRdngCpblties>
Presence: [0..*]
Definition: Card reading capabilities of the POI performing the transaction.
Datatype: "CardDataReading1Code" on page 889
CodeName Name Definition
TAGC Tag Tag reading capabilities (RFID, etc.).
PHYS Physical Keyboard entry or OCR reading of
embossing or printed data, either at time
of transaction or after the event.
BRCD BarCode Bar code.
MGST MagneticStripe Magnetic stripe.
CICC ICC ICC (Integrated Circuit Card) with
contact containing software applications
conform to ISO 7816.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
502 March 2026
```

