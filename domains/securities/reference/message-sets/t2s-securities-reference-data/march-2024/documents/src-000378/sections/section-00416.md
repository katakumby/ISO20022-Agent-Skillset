---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.2 CodeSet", "13.2.2.5 Appearance1Code"]
file_pages: [509]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.2.5 Appearance1Code

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 509 to 509.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 509

```text
CodeName Name Definition
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
13.2.2.5  Appearance1Code
Definition: Specifies the deliverability of a security.
Type: CodeSet
CodeName Name Definition
DELI Deliverable Physical certificates exist.
NDEL NotDeliverable Not yet deliverable contract.
LIMI Limited Limited or partial deliverability.
BENT BookEntry Security exists only as an electronic
record, ie, there are no physical
certificates representing the security.
DFBE DeferredBookEntry Deferred printing, book entry.
DLBE DeliverableBookEntry Deliverable, book entry.
TMPG TemporaryGlobal Deferred printing, global certificate.
GLOB Global Not deliverable, global certificate.
13.2.2.6  AssignmentMethod1Code
Definition: Method under which assignment was conducted.
Type: CodeSet
CodeName Name Definition
RAND Random Assignment was conducted randomly.
PROR Prorata Assignment was conducted on a prorata
basis.
13.2.2.7  BenchmarkCurveName1Code
Definition: Identifies a benchmark curve name.
Type: CodeSet
CodeName Name Definition
MAAA MuniAAA Benchmark curve used for municipals
based on the best credit rating for
municipal market debt.
FUSW FutureSWAP Portion of a synthetic curve that is
composed of Eurodollar or Treasury or
similar Futures and Swap rates. The
term usually begins at 3 months to 2
years for the futures strip component
with the Swaps filling in the points to 10
years and beyond.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 509 March 2024
```

