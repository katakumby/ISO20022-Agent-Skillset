---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.5 IdentifierSet", "66.2.5.16 EuroclearClearstreamIdentifier"]
file_pages: [5393]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.5.16 EuroclearClearstreamIdentifier

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5393 to 5393.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5393

```text
66.2.5.16  EuroclearClearstreamIdentifier
Definition: Identifier of securities issued in Luxembourg. The common code is a 9-digit code that
replaces the CEDEL (Clearstream) and Euroclear codes.
Type: IdentifierSet
Identification scheme: Clearstream; EuroclearClearstreamIdentifier
Format
minLength 1
maxLength 12
66.2.5.17  ExtensiveBranchNetworkIdentifier
Definition: The extensive branch network list of the Australian Bank State Branch (BSB) Code. The
codes are used for identifying Australian financial institutions, as assigned by the Australian Payments
Clearing Association (APCA).
Type: IdentifierSet
Identification scheme: Australian Payments Clearing Association (APCA); Australian BSB
Format
pattern AU[0-9]{6,6}
66.2.5.18  FedwireRoutingNumberIdentifier
Definition: Fedwire Routing Number. Identifies financial institutions, in the US, on the FedWire system.
The routing number is assigned by the American Bankers Association (ABA).
Type: IdentifierSet
Identification scheme: US Federal Reserve Bank ; FedwireRoutingNumberIdentifier
Format
pattern FW[0-9]{9,9}
66.2.5.19  GermanBankleitzahlIdentifier
Definition: German Bankleitzahl. Identifies German financial institutions on the German national clearing
systems.
Type: IdentifierSet
Identification scheme: Deutsche Bundesbank ; German Bankleitzahl
Format
pattern BL[0-9]{8,8}
66.2.5.20  HellenicBankIdentificationCodeIdentifier
Definition: Hellenic Bank Identification Code Identifier. Identifies Greek financial institutions on the
Greek national clearing system.
Type: IdentifierSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5393 May 2026
```

