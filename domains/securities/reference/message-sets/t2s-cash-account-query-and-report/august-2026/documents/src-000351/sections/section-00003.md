---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [3]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02", "acmt.026.001.02", "reda.038.001.01", "reda.039.001.01", "reda.040.001.01"]
---

# 1 Message Set Overview

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 3 to 3.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Cash Account Query and Report message set. It
includes the query report MessageDefinitions that have been developed in the scope of the Target2-
Securities Business Justification (See BJ#042) and approved by the Securities SEG on 18 June 2026.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
acmt.025.001.02
AccountQueryListV02
This message is a query message with specification of
requested accounts, and requested characteristics.
acmt.026.001.02
AccountListReportV02
This message is sent in response to a query message,
and contains the list of requested accounts, with
requested characteristics.
reda.038.001.01
CashAccountActivityAdviceV01
The CashAccountActivityReport message is sent by
the executing party to an instructing party containing
information about changes on cash account reference
data.
Scope and usage:
It aims at informing about the changes occurred during
a business date for cash account reference data.
reda.039.001.01
CashAccountAuditTrailQueryV01
The CashAccountAuditTrailQuery message is sent by
an instructing party to the executing party to query for
the cash account audit trail recorded in the system.
reda.040.001.01
CashAccountAuditTrailReportV01
The CashAccountAuditTrailReport message is sent by
the executing party to an instructing party to provide
detailed information on the requested cash account
audit trail recorded in the system.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Set Overview
Target2-Securities - Cash Account Query and Report 3 August 2026
```

