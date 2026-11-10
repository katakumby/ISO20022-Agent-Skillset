---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "2.3 Constraints"]
file_pages: [11]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.02"]
---

# 2.3 Constraints

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 11 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 11

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     BusinessService <BizSvc> [0..1] Text 20
     CreationDate <CreDt> [1..1] DateTime 20
     CopyDuplicate <CpyDplct> [0..1] CodeSet 20
     PossibleDuplicate <PssblDplct> [0..1] Indicator 21
     Priority <Prty> [0..1] CodeSet C7 21
     Signature <Sgntr> [0..1] (External Schema) 22
2.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 OnlySignatureElement
The XML Signature namespace ("http://www.w3.org/2000/09/xmldsig#") allows for different
XML elements to be root elements. This means the user has to choose amongst these global
elements which one to use as the root element. Only the XML element Signature is allowed.
C5 RelatedPresentWhenCopyDupl
Related MUST contain the relevant BusinessMessageHeader elements of the
BusinessMessage to which this BusinessMessage relates.
If CopyDuplicate is present, then Related MUST be present.
On Condition
    /CopyDuplicate is present
Following Must be True
    /Related[1] Must be present
This constraint is defined at the MessageDefinition level.
C6 ValidationByTable
C7 ValidationByTable
Approved by the Securities SEG on 27 January 2026 head.001.001.02 BusinessApplicationHeaderV02
Corporate Actions - Maintenance 2025 - 2026 11 February 2026
```

